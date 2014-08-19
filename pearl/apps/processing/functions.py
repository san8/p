"""
Helper fucntions for Quality control & Processing.
"""

from os.path import join
from os import listdir, devnull, getcwd, chdir 
from subprocess import call
from contextlib import contextmanager
from pearl.settings.base import NEW_PROJECT_DIR


@contextmanager
def cd(path):
    """
    A simple context manager to change directory.
    """
    old_dir = getcwd()
    chdir(path)
    try: yield
    finally: chdir(old_dir)


def do_qc(project_id):
    """
    Uzip user files and start quality control. 
    """
    from apps.project.models import NewProject
    project = NewProject.objects.get(pk=project_id)
    project_dir = join(NEW_PROJECT_DIR, str(project_id))
    unzip_files(project_dir)
    quality_control = {'fastq': fastq_qc, 'vcf': vcf_qc}
    quality_control[project.file_type](project_dir)
    project.status = 2
    project.save()
    return True


def unzip_files(path):
    """
    Unzip the files in the given location & remove zip files.
    """
    zip_files = [files for files in listdir(path)]
    with cd(path):
        for zip_file in zip_files:
            commands = [["7z", "e", zip_file], ["rm", zip_file]]
            for command in commands:
                call(command, stdout=open(devnull, 'wb'))
    return True

def fastq_qc(project_dir):
    """
    Run FASTQC on unzipped files to generate qc report.
    """
    fastq_files = [files for files in listdir(project_dir)]
    with cd(project_dir):
        for fastq_file in fastq_files: 
            command = ["fastqc", fastq_file, "--quiet"]
            call(command, stdout=open(devnull, 'wb'))
    return True

def vcf_qc(project_id):
    """
    Do QC for VCF files.
    """


def user_approval(project_id):
    """
    Wait for user approval for further processing.
    """


def do_processing(project_id):
    pass 
