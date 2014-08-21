"""
All celery tasks required for projects. 
"""

from celery import Celery
from shutil import copyfileobj
from urllib2 import urlopen

from .functions import get_files


celery = Celery('project_tasks', include=['apps.processing.tasks'])

'''
celery = Celery(name = 'project_tasks', backend='amqp', broker='amqp://,
              include['apps.processing.tasks'])
'''

@celery.task()
def project_tasks(project_id, project_status):
    """
    Call a corresponding fucntion when status is changed.
    """
    if project_status == 0:
        get_files(project_id)
    print project_id, project_status
    return True


@celery.task()
def fetch_files_ftp(local_dir, url_list):
    """
    Gets files from url_list and stores them in local_dir. 
    """
    from apps.processing.functions import cd
    with cd(local_dir):
        for url in url_list:
            ftp_file = urlopen(url)
            local_file_name = url.split('/')[-1]
            local_file = open(local_file_name, "wb") 
            copyfileobj(ftp_file, local_file)
    return True


