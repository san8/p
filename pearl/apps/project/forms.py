from django import forms

from .models import (Project, VCF_UPLOAD_CHOICES, FILE_TYPE_CHOICES,
                     NUMBER_OF_FASTQ, PROCESSING_CHOICES)


class ProjectForm(forms.ModelForm):

    file_type = forms.ChoiceField(choices=FILE_TYPE_CHOICES,
                                  widget=forms.RadioSelect,)
    vcf_upload_type = forms.ChoiceField(choices=VCF_UPLOAD_CHOICES,
                                        widget=forms.RadioSelect,
                                        initial=3)
    total_fastq_files = forms.ChoiceField(choices=NUMBER_OF_FASTQ,
                                          widget=forms.RadioSelect,
                                          initial=1)
    vcf_file = forms.FileField(required=False)

    class Meta:
        model = Project
        fields = ['name', 'description', 'file_type',
                  'total_fastq_files', 'fastq_file1',
                  'fastq_file2', 'vcf_upload_type', 'vcf_file',
                  'paired_end_distance', 'vcf_file1', 'disease', 'tissue']

    def clean_disease(self):
        disease = self.cleaned_data['disease']
        from .models import MeshDiseases
        if disease and not MeshDiseases.objects.filter(
                descriptornamestring=disease).exists():
            raise forms.ValidationError(
                "Please select standard disease from MeSH drop down.")


class StartProcessingForm(forms.ModelForm):

    start_processing = forms.TypedChoiceField(
        choices=PROCESSING_CHOICES,
        widget=forms.RadioSelect, coerce=int, required=True,)

    class Meta:
        model = Project
        fields = ['start_processing']
