from os.path import isfile, join, splitext 
from os import chdir, getcwd, listdir, mkdir 
from contextlib import contextmanager
from subprocess import call 
from celery import Celery 

from pearl.settings import BASE_DIR 


app = Celery('project_tasks', backend='amqp', broker='amqp://')

@app.task()
def do_processing(project_id):
    # quality control, report, vcf, final report
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 1:
        do_quality_control.apply_async(args=[project_id,]) 
        """
        chain = do_quality_control.s(project_id,) 
        chain() 
        """
        return 'Successfully completed do_processing'
    else:
        return 'Project status is NOT ONE'


@contextmanager
def cd(path):
    old_dir = getcwd()
    chdir(path)
    try:
        yield
    finally:
        chdir(old_dir)


@app.task()
def do_quality_control(project_id):
    # unzip file, do qc
    from apps.project.models import NewProject 
    project = NewProject.objects.get(id=project_id)
    if project.status == 1:
        local_dir = join(BASE_DIR, 'files/NewProject/', str(project_id)) 
        with cd(local_dir):
            files = [f for f in listdir(local_dir) if isfile(join(local_dir, f))]
            for zip_file in files:
                print zip_file 
                call(["7z","e", zip_file])
            files = [f for f in listdir(getcwd()) if isfile(join(local_dir, f))]
            report_dir = join(BASE_DIR, "files/Report/", str(project_id))
            mkdir(report_dir)
            for local_file in files:
                if  splitext(local_file)[1] == '.fastq':
                    call(["fastqc", local_file, "-o", report_dir, "-q"])
        project.status = 2
        project.save()
        return 'Successfully complted QC.'
    else:
        return "Project status NOT ONE. do_quality_control"


"""
@app.task(name='apps.project.tasks.do_qc')
def do_qasdfuality_control(project_id):
    pass 
STATUS = ('Uploading RAW Files.',
          'QC Processing.',
          'Started Processing.',
          'Completed.')
"""
