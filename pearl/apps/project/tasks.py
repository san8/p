"""
Celery tasks to fetch files and do quality check.
"""

from __future__ import absolute_import

import logging
import os
import shutil
import subprocess
from contextlib import contextmanager
from os.path import join
from shutil import copyfileobj
from urllib2 import urlopen

from django.db import connection

from apps.processing.tasks import processing
from pearl.celery_conf import app as celery_app
from pearl.settings.base import BASE_DIR, PROJECTS_DIR


logger = logging.getLogger(__name__)

celery_app.conf.update(
    CELERYD_LOG_COLOR=False,
    CELERYD_POOL_RESTARTS=True,
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE="UTC",
)


@celery_app.task()
def project_queue(project_id, project_status, file_type):
    """
    Queue up all projects by calling tasks based on status.
    """
    if project_status == 5:
        queue = 'ftp_' + file_type
        ftp_qc.apply_async(args=[project_id], queue=queue)
    elif project_status == 20:
        processing.apply_async(args=[project_id, file_type], queue='proc')
    return project_id, project_status


@celery_app.task()
def ftp_qc(project_id):
    """
    Fectch project files, do_qc  & update project status.
    """
    from .models import Project
    connection.close()
    project = Project.objects.get(id=project_id)
    url_list = filter(None, [project.fastq_file1, project.fastq_file2,
                             project.vcf_file1])
    print(url_list)
    local_dir = join(PROJECTS_DIR, str(project_id))
    os.mkdir(local_dir)
    os.chmod(local_dir, 0777)
    try:
        if project.vcf_upload_type == 3:
            fetch_files_ftp(local_dir, url_list)
        elif project.vcf_upload_type == 4:
            move_file(local_dir, project.vcf_file.path)
        unzip_files(local_dir)
        result = unicode_check(local_dir)
        if result:
            pass
        else:
            new_status = update_status(project_id, -7)
    except:
        new_status = update_status(project_id, -6)
        return project_id, new_status

    if project.file_type == 'fastq':
        try:
            do_qc(project_id, project.file_type)
            new_status = update_status(project_id, 15)
            print(project_id, new_status)
        except:
            new_status = update_status(project_id, -11)
            return project_id, new_status

    new_status = update_status(project_id, 20)  # bypass user approval
    print(project_id, new_status)
    return "ftp_qc completed successfully."


def unicode_check(local_dir):
    """
    Find if unicode chars are present in given files.

    :param local_dir: path to any directory.
    :return: True if unicode is absent, otherwise False.
    """
    files = [os.path.join(local_dir, f) for f in os.listdir(local_dir)]
    for f in files:
        command = "/usr/bin/filter.pl -f " + f
        result = subprocess.call(command, shell=True)
        if result != 0:
            return False
    return True


def update_status(project_id, status):
    """
    Change status of given project.
    """
    from apps.project.models import Project
    connection.close()
    project = Project.objects.get(id=project_id)
    project.status = status
    project.save()
    return status


def status(project_id):
    from apps.project.models import Project
    connection.close()
    project = Project.objects.get(id=project_id)
    return project.status


@contextmanager
def cd(path):
    """
    A simple context manager to change directory.
    """
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)


def fetch_files_ftp(local_dir, url_list):
    """
    Gets files from url_list and stores them in local_dir.
    """
    with cd(local_dir):
        for url in url_list:
            ftp_file = urlopen(url)
            local_file_name = url.split('/')[-1]
            local_file = open(local_file_name, "wb")
            copyfileobj(ftp_file, local_file)
    return True


def move_file(local_dir, file_path):
    """
    Move vcf file from temporary location to project dir.
    """
    # logger.info(local_dir, file_path)
    print(local_dir, file_path)
    shutil.move(file_path, local_dir)


def do_qc(project_id, file_type):
    """
    Uzip user files and start quality control.
    """
    project_dir = join(PROJECTS_DIR, str(project_id))
    if file_type == 'fastq':
        fastq_qc(project_dir)
        fastq_qc_plus(project_dir)
    return True


def unzip_files(path):
    """
    Unzip the files in the given location & delete zip files.
    """
    zip_files = [files for files in os.listdir(path)]
    with cd(path):
        for zip_file in zip_files:
            commands = [["7z", "e", zip_file], ["rm", zip_file]]
            try:
                for command in commands:
                    subprocess.call(command, stdout=open(os.devnull, 'wb'))
            except:
                pass
    return True


def fastq_qc(project_dir):
    """
    Run FASTQC on unzipped files to generate qc report.
    """
    fastq_files = [files for files in os.listdir(project_dir)]
    fastqc = os.path.join(BASE_DIR, 'bin/fastqc/fastqc')
    with cd(project_dir):
        for fastq_file in fastq_files:
            command = [fastqc, fastq_file, "--extract", "--quiet"]
            subprocess.call(command, stdout=open(os.devnull, 'wb'))
    return True


def fastq_qc_plus(project_id):
    """
    Parse FASTQC results & get base statistics, sequence quality,
    length distribution, adapter content
    """
    project_dir = join(PROJECTS_DIR, str(project_id))
    with cd(project_dir):
        qc_data = []
        for root, dirs, files in os.walk(project_dir):
            for file_name in files:
                if file_name == 'fastqc_data.txt':
                    data = parse_data(join(root, file_name))
                    qc_data.append(data)
    return qc_data


def parse_data(file_name):
    """
    Parse fastqc_data file and return only required values.
    """
    from fadapa import Fadapa
    d = Fadapa(file_name)
    data = {}
    data['base_stats'] = d.clean_data('Basic Statistics')[1:]

    base_n = d.clean_data('Per base N content')[1:]
    base_n = [[int(x[0]), float(x[1])] for x in base_n]
    data['base_n'] = base_n

    base_seq = d.clean_data('Per base sequence quality')[1:]
    base_seq = [[int(x[0]), float(x[1])] for x in base_seq]
    data['base_seq'] = base_seq

    try:
        data['adapter'] = d.cleaned_data('Adapter Content')[1:]
    except:
        pass

    return data
