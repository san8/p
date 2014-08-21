"""
All helper functions for work flow. 
"""

from os import mkdir
from os.path import join

from pearl.settings.base import NEW_PROJECT_DIR


def get_files(project_id):
    """
    Gets user files & updates status.
    """
    from .models import NewProject 
    from .tasks import fetch_files_ftp

    project = NewProject.objects.get(id=project_id)
    url_list = [project.fastq_file1, project.fastq_file2, project.vcf_file1] 
    url_list = filter(None, url_list)
    local_dir = join(NEW_PROJECT_DIR, str(project_id)) 
    mkdir(local_dir)
    fetch_files_ftp.s(local_dir, url_list)() 
    import time
    time.sleep(20)
    project.status = 1
    project.save()
    return True
    
