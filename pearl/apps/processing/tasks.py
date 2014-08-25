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
    else:
        print 'started vcf processing'
        import time
        time.sleep(10)
        print 'completed vcf processing'
    return True
        
