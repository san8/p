from django.forms import ModelForm 

from .models import NewProject 


class NewProjectForm(ModelForm):
    class Meta:
        model = NewProject
        fields = ['name', 'description', 'file_type',
                  'total_fastq_files', 'fastq_file1', 'file1_read', 
                  'fastq_file2', 'file2_read', 'vcf_file1',
                  'tissue', 'disease']

        def __unicode__(self):
            return self.name


""" 
from django.forms import ModelForm
from project.models import NewProject

class NewProjectForm(ModelForm):
    class meta:
        model = NewProject
        fields = ['name', 'description', 'file_type', 'vcf_file',
                  'total_fastq_files', 'fastq_file1', 'fastq_file2',
                  'tissue', 'disease']

""" 

