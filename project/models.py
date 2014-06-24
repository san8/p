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
            default=''
        )
    vcf_file = models.FileField(
            upload_to = 'documents/%Y/%m/%d',
            blank=True
        )
    total_fastq_files = models.CharField(
            max_length=2, choices=TOTAL_FASTQ_FILES,
            default=''
        )
    fastq_file1 = models.URLField(max_length=200, blank=True)
    fastq_file2 = models.URLField(max_length=200, blank=True)
    tissue = models.CharField(
            max_length=30, choices=TISSUE_CHOICES,
            default=''
        )
    disease = models.CharField(
            max_length=100, choices=DISEASE_CHOICES,
            default=''
        )

    def __unicode__(self):
        return self.name 


class NewProjectForm(ModelForm):
    class Meta:
        model = NewProject
        fields = ['name', 'description', 'file_type', 'vcf_file',
                  'total_fastq_files', 'fastq_file1', 'fastq_file2',
                  'tissue', 'disease']

        def __unicode__(self):
            return self.name


