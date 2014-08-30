from celery import Celery

celery = Celery('processing_tasks',backend='amqp', broker='amqp://',
                include=['apps.project.tasks'],)


@celery.task()
def processing(project_id, file_type):
    if file_type == 'fastq':
        print 'started fastq processing'
        import time
        time.sleep(20)
        print 'completed fastq processing'
        fastq_processing(project_id)
    else:
        print 'started vcf processing'
        import time
        time.sleep(10)
        print 'completed vcf processing'
        vcf_processing.apply_async(args=[project_id,])
    return True


@celery.task()
def fastq_processing(project_id):
    """
    Do fastq processing.
    """
    print("fast_processing func")
    pass


@celery.task()
def vcf_processing(project_id):
    """
    Do VCF processing.
    """
    pass

    
