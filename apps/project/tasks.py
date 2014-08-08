"""
All celery tasks required for projects. 
"""

from celery import Celery
from contextlib import contextmanager
from os import getcwd, chdir
from shutil import copyfileobj
from urllib2 import urlopen

from .functions import get_files
from apps.processing.functions import do_qc, do_processing

celery = Celery('project_tasks', backend='amqp', broker='amqp://',
                 include=['apps.processing.tasks'])


@celery.task()
def work_flow(project_id, project_status):
    """
    Call a corresponding fucntion when status is changed.
    """
    print project_status, project_id
    if project_status in range(0,3):
        functions = [get_files, do_qc, None, do_processing]
        functions[project_status](project_id)


@contextmanager
def cd(path):
    """
    Simple context manager to change directory. 
    """
    old_dir = getcwd()
    chdir(path)
    try: yield 
    finally: chdir(old_dir)


@celery.task()
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
    print "Successfully fetched FTP files."


'''
@celery.task()
def add(x, y):
    return x + y


@celery.task()
def add_db(id):
    from .models import NewProject
    x = id
    n = NewProject.objects.get(pk=id)
    y = n.customer_id
    return x + y 

@celery.task()
def test():
    sleep(100000)
    pass 
'''
