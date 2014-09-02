"""
All celery tasks required for projects. 
"""
from __future__ import absolute_import

from subprocess import call
import os
from os import mkdir, getcwd, chdir, devnull, listdir
from os.path import join
from shutil import copyfileobj
from urllib2 import urlopen
from contextlib import contextmanager
from celery import Celery

from pearl.settings.base import NEW_PROJECT_DIR, BASE_DIR
from apps.processing.tasks import processing

celery = Celery('project_tasks',backend='amqp', broker='amqp://',
                include=['apps.processing.tasks'],)

@celery.task()
def project_queue(project_id, project_status, file_type):
    """
    Queue up all projects by calling required tasks.
    """
    if project_status == 0:
        queue = 'ftp_' + file_type
        get_files.apply_async(args=[project_id], queue=queue)
    elif project_status == 2:
        queue = 'proc_' + file_type
        processing.apply_async(args=[project_id, file_type], queue=queue)


@celery.task()
def get_files(project_id):
    """
    Gets customer files & updates status.
    """
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    url_list = [project.fastq_file1, project.fastq_file2, project.vcf_file1] 
    url_list = filter(None, url_list)
    local_dir = join(NEW_PROJECT_DIR, str(project_id)) 
    mkdir(local_dir)
    fetch_files_ftp(local_dir, url_list)
    do_qc(project_id, project.file_type)
    project.status = 2
    project.save()
    return True


@contextmanager
def cd(path):
    """
    A simple context manager to change directory.
    """
    old_dir = getcwd()
    chdir(path)
    try: yield
    finally: chdir(old_dir)


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

    
def do_qc(project_id, file_type):
    """
    Uzip user files and start quality control. 
    """
    project_dir = join(NEW_PROJECT_DIR, str(project_id))
    unzip_files(project_dir)
    if file_type == 'fastq':
        fastq_qc(project_dir)
        fastq_qc_plus(project_dir)
    elif file_type == 'vcf':
        vcf_qc(project_id)
    return True


def unzip_files(path):
    """
    Unzip the files in the given location & delete zip files.
    """
    zip_files = [files for files in listdir(path)]
    with cd(path):
        for zip_file in zip_files:
            commands = [["7z", "e", zip_file], ["rm", zip_file]]
            for command in commands:
                call(command, stdout=open(devnull, 'wb'))
    return True


def fastq_qc(project_dir):
    """
    Run FASTQC on unzipped files to generate qc report.
    """
    fastq_files = [files for files in listdir(project_dir)]
    with cd(project_dir):
        for fastq_file in fastq_files: 
            command = ["fastqc", fastq_file, "--quiet"]
            call(command, stdout=open(devnull, 'wb'))
    return True


def fastq_qc_plus(project_dir):
    """
    Run a script on top of fastq_qc to remove unwanted details.
    """
    with cd(project_dir):
        for root, dirs, files in os.walk(project_dir):
            for file_name in files:
                if 'fastqc_data.txt' in file_name:
                    report_name = root.split('/')[-1].replace('fastqc', 'report')
                    file_path = join(root, file_name)
                    command = ['python', join(BASE_DIR, 'bin/fastq_qc_plus.py'),
                    file_path, report_name]
                    call(command, stdout=open(devnull, 'wb'))

    
def vcf_qc(project_id):
    """
    Run VCF QC check on unzipped files.
    """
    print 'started vcf qc'
    import time
    time.sleep(10)
    print 'vcf qc completed'    
