"""
Various tasks to process the user files.
"""

import os
import subprocess

from django.db import connection

from pearl.celery_conf import app as celery_app
from pearl.settings.base import PROJECTS_DIR


celery_app.conf.update(
    CELERYD_LOG_COLOR=False,
    CELERYD_POOL_RESTARTS=True,
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE="UTC",
)


@celery_app.task()
def processing(project_id, file_type):
    """
    Route tasks according to their file type.
    """
    if file_type == 'fastq':
        fastq_processing.apply_async(args=[project_id], queue='proc_fastq')
    elif file_type == 'vcf':
        vcf_processing.apply_async(args=[project_id], queue='proc_vcf')
    return True


@celery_app.task()
def fastq_processing(project_id):
    """
    Run fastq through a perl script which runs all the pipelines.
    """
    time_zone = get_timezone(project_id)
    project_dir = os.path.join(PROJECTS_DIR, str(project_id))
    file_name = str(project_id)
    fq_files = [os.path.join(project_dir, f) for f in os.listdir(project_dir)
                if f[-6:] == '.fastq']
    if len(fq_files) == 2:
        command = "workflow.pl -1 " + fq_files[0] + " -2 " + fq_files[1] + \
                  " -o " + project_dir + " -p " + file_name + " -t " + time_zone
    if len(fq_files) == 1:
        command = "workflow.pl -u " + fq_files[0] + " -o " + project_dir + \
                  " -p " + file_name + " -t " + time_zone
    subprocess.call(command, shell=True)
    new_status = update_status(project_id, status=22)
    return project_id, new_status


@celery_app.task()
def vcf_processing(project_id):
    """
    VCF processing through a perl script.
    """
    time_zone = get_timezone(project_id)
    file_name = str(project_id)
    project_dir = os.path.join(PROJECTS_DIR, str(project_id))
    vcf_file = [os.path.join(project_dir, f) for f in os.listdir(project_dir)
                if f[-4:] == '.vcf']
    command = "workflow.pl -v " + vcf_file[0] + ' -o ' + project_dir + \
              " -p " + file_name + " -t " + time_zone
    subprocess.call(command, shell=True)
    new_status = update_status(project_id, status=22)
    return project_id, new_status


def update_status(project_id, status):
    """
    Change status of project.
    """
    from apps.project.models import Project
    connection.close()
    project = Project.objects.get(id=project_id)
    project.status = status
    project.save()
    return status


def get_timezone(project_id):
    """
    Get timezone of customer of the project.
    :param project_id: id of the project.
    :return: timezone
    """
    from apps.project.models import Project
    from apps.accounts.models import Customer
    connection.close()
    user_id = Project.objects.get(id=project_id).user_id
    time_zone = Customer.objects.get(user_id=user_id).timezone
    if not time_zone:
        return 'UTC'
    return time_zone
