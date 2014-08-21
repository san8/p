"""
List of tasks done during processing.
"""

from __future__ import absolute_import
from celery import Celery

from .functions import do_qc


celery = Celery(name='processing_tasks', include=['apps.project.tasks',])


@celery.task()
def processing_tasks(project_id, project_status):
    """
    After qc is completed, send mail to user about it.
    """
    if project_status == 1:
        print 'start processing'
        do_qc(project_id)
        print 'completed processing'
    pass



"""
@app.task()
def report_mail(project_id):
    pass 


@app.task(name='apps.project.tasks.do_qc')
def do_qasdfuality_control(project_id):
    pass 
STATUS = ('Uploading RAW Files.',
          'QC Processing.',
          'Started Processing.',
          'Completed.')
"""
'''
def start_processing(project_id):
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    return project.start_processing 
'''
#chain = check_fastq_quality.s(project_id)
#chain()

"""
@app.task()
def do_qc(project_id):
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    try:
        if project.file_type == 'fastq':
            local_dir = join(BASE_DIR, NEW_PROJECT_DIR, str(project_id)) 
            with cd(local_dir):
                # unzip files
                files = [f for f in listdir(local_dir) if isfile(join(local_dir, f))]
                for zip_file in files:
                    command = ["7z", "e", zip_file]
                    call(command, stdout=open(devnull, 'wb'))
                # run fastqc 
                files = [f for f in listdir(getcwd()) if isfile(join(local_dir, f))]
                report_dir = join(BASE_DIR, REPORT_DIR, str(project_id))
                mkdir(report_dir)
                for local_file in files:
                    if  splitext(local_file)[1] == '.fastq':
                        call(["fastqc", local_file, "-o", report_dir, "-q"])
            project.status = 2
            project.save()
            print 'Successfully completed  FASTQ QC.'
        elif project.file_type == 'vcf':
            print 'Check VCF Quality'
        return 0
    except:
        print('Unable to do QC. ')
        return -1




@app.task()
def do_processing(project_id):
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.file_type == 'fastq':
        print 'Started Processing FASTQ.'
        return 0
"""
