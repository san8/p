from django.db import models
from django.contrib.auth.models import User 
from django.forms import ModelForm 


FILE_TYPE = (
    ('FASTQ', 'FASTQ'),
    ('VCF', 'VCF')
)
TOTAL_FASTQ_FILES = (
    ('1', '1'),
    ('2', '2'),
)
READ_CHOICES = (
    ('Forward', 'Forward'),
    ('Backward', 'Backward')
)
TISSUE_CHOICES = (
    ('Tissue_A', 'TISSUE_A'),
    ('Tissue_B', 'TISSUE_B')
)
DISEASE_CHOICES = (
    ('Disease A', 'Disease A'),
    ('Disease B', 'Disease B'),
)

class NewProject(models.Model):
    customer = models.ForeignKey(User, related_name='original_customer_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    file_type = models.CharField(
            max_length=10, choices=FILE_TYPE,
            default='FASTQ'
        )
    """ 
    vcf_file = models.FileField(
            upload_to = 'documents/%Y/%m/%d',
            blank=True 
        )
    """ 
    total_fastq_files = models.CharField(
            max_length=2, choices=TOTAL_FASTQ_FILES,
            default=''
        )
    fastq_file1 = models.URLField(max_length=200, blank=True)
    file1_read = models.CharField(
            max_length='8', choices = READ_CHOICES,
            default='Forward')
    fastq_file2 = models.URLField(max_length=200, blank=True)
    file2_read = models.CharField(
            max_length='8', choices = READ_CHOICES,
            default='Backward')
    vcf_file1 = models.URLField(max_length=200, blank=True)
    tissue = models.CharField(
            max_length=30, choices=TISSUE_CHOICES,
            default=''
        )
    disease = models.CharField(
            max_length=100, choices=DISEASE_CHOICES,
            default=''
        )
    status = models.CharField(
            max_length=20, default='Raw Files Uploaded'
        )

    def __unicode__(self):
        return self.name 


class NewProjectForm(ModelForm):
    class Meta:
        model = NewProject
        fields = ['name', 'description', 'file_type',
                  'total_fastq_files', 'fastq_file1', 'file1_read', 
                  'fastq_file2', 'file2_read', 'vcf_file1',
                  'tissue', 'disease']

        def __unicode__(self):
            return self.name


