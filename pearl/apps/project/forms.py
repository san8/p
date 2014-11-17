from django import forms 

from .models import NewProject 

FILE_TYPE_CHOICES = (
    ('fastq', 'FASTQ'),
    ('vcf', 'VCF'),
)
NUMBER_OF_FASTQ = (
    ('1', 'Single End'),
    ('2', 'Paired End')
)
PROCESSING_CHOICES = (
    ('1', 'Yes'),
    ('0', 'No'),
)


class NewProjectForm(forms.ModelForm):
                
    file_type = forms.ChoiceField(choices=FILE_TYPE_CHOICES,
                                  widget=forms.RadioSelect,)
    total_fastq_files = forms.ChoiceField(choices=NUMBER_OF_FASTQ,
                                          widget=forms.RadioSelect,
                                          initial=1, )
    class Meta:
        model = NewProject
        fields = ['name', 'description', 'file_type',
                  'total_fastq_files', 'fastq_file1', 
                  'fastq_file2', 'paired_end_distance', 
                  'vcf_file1', 'tissue', 'disease']


class StartProcessingForm(forms.ModelForm):

    start_processing = forms.TypedChoiceField(choices=PROCESSING_CHOICES,
                widget=forms.RadioSelect, coerce=int, required=True,)

    class Meta:
        model = NewProject 
        fields = ['start_processing']

