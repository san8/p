"""
Various tasks to process the user files.
"""

import sys
import os
import subprocess

from pearl.settings.base import NEW_PROJECT_DIR
from pearl.celery_conf import app as celery_app


@celery_app.task()
def processing(project_id, file_type):
    """
    Route tasks according to their file type.
    """
    if file_type == 'fastq':
        fastq_processing.delay(project_id)
    elif file_type == 'vcf':
        vcf_processing.apply_async(args=[project_id,])
    return True


@celery_app.task()
def fastq_processing(project_id):
    """
    Run fastq through a perl script which runs all the pipelines.
    """
    project_dir = os.path.join(NEW_PROJECT_DIR, str(project_id)) 
    print(project_dir)
    fq_files = [ os.path.join(project_dir, f) for f in os.listdir(project_dir) \
                 if f[-6:] == '.fastq' ]
    if len(fq_files) == 2:
        command = ["pearl workflow.pl ", "-1", fq_files[0], "-2", fq_files[1],
                   "-o", project_dir]
    if len(fq_files) == 1:
        command = ["perl workflow.pl", "-u", fq_files[0], "-o", project_dir]
    subprocess.call(command, stdout=open(os.devnull, 'wb'))
    return True


@celery_app.task()
def vcf_processing(project_id):
    """
    Do VCF processing.
    """
    update_status(project_id, 4)
    print('completed vcf_processing func')

    
def update_status(project_id, status):
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    project.status = status
    print(project_id, status)
    project.save()
    
