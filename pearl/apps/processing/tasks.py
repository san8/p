import sys

from pearl.celery_conf import app as celery_app


@celery_app.task()
def processing(project_id, file_type):
    import time
    time.sleep(10)
    if file_type == 'fastq':
        fastq_processing(project_id)
    else:
        vcf_processing.apply_async(args=[project_id,])
    return True


@celery_app.task()
def fastq_processing(project_id):
    """
    Do fastq processing.
    """
    update_status(project_id, 4)
    print(sys._getframe().f_code.co_name)


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
    
