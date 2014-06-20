from django.db import models
from home.models import Customers


class NewProject(models.Model):
    customer_id = models.OneToOneField(Customers, null=True)
    name = models.CharField(max_length = 100, default='')
    description = models.CharField(max_length = 100, default = '')
    upload_file = models.FileField(
            upload_to = 'documents/%Y/%m/%d',
            default = ''
            )
    ftp_file = models.URLField(max_length = 50, default = '')
    tissue = models.CharField(max_length = 30, default='')
    disease = models.CharField(max_length = 30, default='')
    optional = models.CharField(max_length = 30, default='')
    status = models.CharField(max_length = 30, default='')


class Document(models.Model):
    status = models.CharField(max_length = 30, default='')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
