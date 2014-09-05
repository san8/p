from pearl.celery_conf import app as celery_app

@celery_app.task()
def processing(project_id, file_type):
    if file_type == 'fastq':
        print 'started fastq processing'
        import time
        time.sleep(5)
        print 'completed fastq processing'
        fastq_processing(project_id)
    else:
        print 'started vcf processing'
        import time
        time.sleep(5)
        print 'completed vcf processing'
        vcf_processing.apply_async(args=[project_id,])
    return True


@celery_app.task()
def fastq_processing(project_id):
    """
    Do fastq processing.
    """
    print("fast_processing func")
    pass


@celery_app.task()
def vcf_processing(project_id):
    """
    Do VCF processing.
    """
    pass

    
