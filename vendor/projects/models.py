from django.db import models
from django.contrib.auth.models import User 


class NewProject(models.Model):
    customer = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    upload_file = models.FileField(
            upload_to = 'documents/%Y/%m/%d',
            default = ''
        )
    ftp_file = models.URLField(max_length = 50, default = '')
    TISSUE_CHOICES = (
            ('Tissue_A', 'TISSUE_A'),
            ('Tissue_B', 'TISSUE_B')
        )
    tissue = models.CharField(
            max_length=30, choices=TISSUE_CHOICES,
            default=''
        )
    disease = models.CharField(max_length = 30, default='')
    optional = models.CharField(max_length = 30, default='')
    status = models.CharField(max_length = 30, default='')


class Document(models.Model):
    status = models.CharField(max_length = 30, default='')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
