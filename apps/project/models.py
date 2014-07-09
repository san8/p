from django.contrib.auth.models import User 
from django.db import models
from django.db.models import signals 

from .tasks import get_ftp_files 


FILE_TYPE = (
    ('FASTQ', 'FASTQ'),
    ('VCF', 'VCF'), 
)
TOTAL_FASTQ_FILES = (
    ('1', '1'),
    ('2', '2'),
)
READ_CHOICES = (
    ('Forward', 'Forward'),
    ('Backward', 'Backward'), 
)
TISSUE_CHOICES = (
    ('Tissue_A', 'TISSUE_A'),
    ('Tissue_B', 'TISSUE_B'),
)
DISEASE_CHOICES = (
    ('Disease A', 'Disease A'),
    ('Disease B', 'Disease B'),
)

""" 
def update_status(id=132, status_code=2):
    project = NewProject.objects.get(pk=id)
    project.status = 'Started processing.'
    project.save()

""" 
def project_created(sender, instance, created, **kwargs):
    if instance.status == 'Started processing.':
        return 
    else:
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
        instance.status = 'Started processing.'
        instance.save() 


class NewProject(models.Model):
    customer = models.ForeignKey(User, related_name='original_customer_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    file_type = models.CharField(max_length=10, default='FASTQ', 
            choices=FILE_TYPE,)
    """ 
    vcf_file = models.FileField(
            upload_to = 'documents/%Y/%m/%d',
            blank=True 
        )
    """ 
    total_fastq_files = models.CharField(max_length=1, default='1',
            choices=TOTAL_FASTQ_FILES,)
    fastq_file1 = models.URLField(max_length=200, blank=True)
    file1_read = models.CharField(max_length='8', default='Forward',
            choices = READ_CHOICES,)
    fastq_file2 = models.URLField(max_length=200, blank=True)
    file2_read = models.CharField(max_length='8',  default='Backward',
            choices = READ_CHOICES,)
    vcf_file1 = models.URLField(max_length=200, blank=True)
    tissue = models.CharField(max_length=30, default='',
            choices=TISSUE_CHOICES,)
    disease = models.CharField(max_length=100, default='',
            choices=DISEASE_CHOICES,)
    status = models.CharField(max_length=20, default='Raw Files Uploaded',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name 

    class Meta:
        ordering = ['updated_at']

signals.post_save.connect(project_created, sender=NewProject)


class ProjectReport(models.Model):
    project = models.ForeignKey(NewProject, related_name='project_as_foreign_key')
    pdf_file = models.CharField(max_length=100, default='')
    data = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return self.project.name 










