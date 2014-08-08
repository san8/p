"""
Helper fucntions for Quality control & Processing.
"""

from os.path import join, isfile
from os import listdir, devnull
from subprocess import call

from pearl.settings.base import NEW_PROJECT_DIR


def do_qc(project_id):
    """
    Does quality control for user files.
    """
    from apps.project.models import NewProject
    project = NewProject.objects.get(pk=project_id)
    project_dir = join(NEW_PROJECT_DIR, str(project_id))
    quality_control = {'fastq': fastq_qc, 'vcf': vcf_qc}
    quality_control[project.file_type](project_dir)

    
def fastq_qc(project_dir):
    zip_files = [files for files in listdir(project_dir)]
    print zip_files
    for zip_file in zip_files:
        command = ["7z", "e", zip_file]
        print command
        call(command, stdout=open(devnull, 'wb'))
    print 'adfasdlf'
    zip_files = [files for files in listdir(project_dir)]
    print zip_files
    pass 


def vcf_qc():
    pass 


def do_processing(project_id):
    print 'processing'
    pass 
