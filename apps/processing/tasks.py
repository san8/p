from os.path import isfile, join, splitext 
from os import chdir, getcwd, listdir, mkdir 
from contextlib import contextmanager
from subprocess import call 
from celery import Celery 

from pearl.settings import BASE_DIR, NEW_PROJECT_DIR, REPORT_DIR 


app = Celery('project_tasks', backend='amqp', broker='amqp://')

@app.task()
def do_processing(project_id):
    # quality control, report, vcf, final report
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 1:
        if project.file_type == 'fastq':
            chain = check_fastq_quality.s(project_id)
            chain()
            #check_fastq_quality.apply_async(args=[project_id,]).get() 
        elif project.file_type == 'vcf':
            check_vcf_quality.apply_async(args=[project_id,])
        print 'Successfully completed do_processing'
        return 0
    else:
        print('Project status is NOT ONE')
        return 1


@contextmanager
def cd(path):
    old_dir = getcwd()
    chdir(path)
    try:
        yield
    finally:
        chdir(old_dir)


@app.task()
def check_fastq_quality(project_id):
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 1:
        local_dir = join(BASE_DIR, NEW_PROJECT_DIR, str(project_id)) 
        with cd(local_dir):
            # unzip files
            files = [f for f in listdir(local_dir) if isfile(join(local_dir, f))]
            for zip_file in files:
                print zip_file 
                call(["7z","e", zip_file])
            # run fastqc 
            files = [f for f in listdir(getcwd()) if isfile(join(local_dir, f))]
            report_dir = join(BASE_DIR, REPORT_DIR, str(project_id))
            mkdir(report_dir)
            for local_file in files:
                if  splitext(local_file)[1] == '.fastq':
                    call(["fastqc", local_file, "-o", report_dir, "-q"])
        project.status = 2
        project.save()
        print 'Successfully complted QC.'
        return 0
    else:
        print "Project status NOT ONE. do_quality_control"
        return 1


@app.task()
def generate_vcf(project_id):
    pass


@app.task()
def check_vcf_quality(project_id):
    print('checking vcf quality')
    pass


@app.task()
def generate_final_report(project_id):
    pass 


"""
@app.task(name='apps.project.tasks.do_qc')
def do_qasdfuality_control(project_id):
    pass 
STATUS = ('Uploading RAW Files.',
          'QC Processing.',
          'Started Processing.',
          'Completed.')
"""
