from django.dispatch import receiver, Signal 
from django.db.models.signals import post_save 

from .tasks import get_ftp_files 

project_cre = Signal(providing_args=["request", "user"])

@receiver(post_save)
def project_created(sender, instance, created, **kwargs):
    project = NewProject.objects.get(id=instance.id)
    url_list = []
    if project.fastq_file1:
        if project.fastq_file2:
            url_list = [project.fastq_file1, project.fastq_file2]
        else:
            url_list = [project.fastq_file1]
    elif project.vcf_file1:
        url_list = [project.vcf_file1,]
    if url_list: 
        get_ftp_files.apply_async(args=[project.id, url_list,])
