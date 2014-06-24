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
