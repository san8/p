from django import forms

from .models import (NewProject, VCF_UPLOAD_CHOICES, FILE_TYPE_CHOICES,
                     NUMBER_OF_FASTQ, PROCESSING_CHOICES)


class NewProjectForm(forms.ModelForm):

    file_type = forms.ChoiceField(choices=FILE_TYPE_CHOICES,
                                  widget=forms.RadioSelect,)
    vcf_upload_type = forms.ChoiceField(choices=VCF_UPLOAD_CHOICES,
                                        widget=forms.RadioSelect,
                                        required=False)
    total_fastq_files = forms.ChoiceField(choices=NUMBER_OF_FASTQ,
                                          widget=forms.RadioSelect,
                                          initial=1)
    vcf_file = forms.FileField(required=False)

    class Meta:
        model = NewProject
        fields = ['name', 'description', 'file_type',
                  'total_fastq_files', 'fastq_file1',
                  'fastq_file2', 'vcf_upload_type', 'vcf_file',
                  'paired_end_distance', 'vcf_file1', 'tissue', 'disease']


class StartProcessingForm(forms.ModelForm):

    start_processing = forms.TypedChoiceField(choices=PROCESSING_CHOICES,
                widget=forms.RadioSelect, coerce=int, required=True,)

    class Meta:
        model = NewProject
        fields = ['start_processing']
