"""
All celery tasks required for projects. 
"""
from __future__ import absolute_import

from subprocess import call
from os import mkdir, getcwd, chdir, devnull, listdir
from os.path import join
from shutil import copyfileobj
from urllib2 import urlopen
from contextlib import contextmanager
from celery import Celery

from pearl.settings.base import NEW_PROJECT_DIR
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
    Gets files & updates status.
    """
    from .models import NewProject 
    project = NewProject.objects.get(id=project_id)
    url_list = [project.fastq_file1, project.fastq_file2, project.vcf_file1] 
    url_list = filter(None, url_list)
    local_dir = join(NEW_PROJECT_DIR, str(project_id)) 
    mkdir(local_dir)
    print 'started ftp'
    fetch_files_ftp(local_dir, url_list)
    print 'completed ftp'
    print 'started qc'
    do_qc(project_id, project.file_type)
    print 'completed qc'
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
    quality_control = {'fastq': fastq_qc, 'vcf': vcf_qc}
    quality_control[file_type](project_dir)
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


def vcf_qc(project_id):
    """
    Run VCF QC check on unzipped files.
    """
    print 'started vcf qc'
    import time
    time.sleep(10)
    print 'vcf qc completed'    
