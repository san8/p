from django import forms

"""
from django.forms import ModelForm
from projects.models import NewProject

class NewProjectForm(ModelForm):
    class Meta:
        model = NewProject


class NewProjectForm(forms.Form):
    docfile = forms.FileField(
        label = 'Select file to upload',
    )
"""

class NewProjectForm(forms.Form):
    name = forms.CharField(max_length = 100)
    description = forms.CharField(max_length = 100)
    upload_file = forms.FileField(label = 'Upload File')
    FTP_file = forms.URLField(max_length = 50)
    tissues = forms.ChoiceField(
        choices=[('Tissue A', 'Tissue A'),
                 ('Tissue B', 'Tissue B')]
    )
    disease = forms.ChoiceField(
        choices = [('Disease A', 'Disease A'),
                   ('Disease B', 'Disease B')]
    )


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        pass


class DocumentForm(forms.Form):
    status = forms.CharField(max_length=100)
    docfile = forms.FileField(label='select file')

