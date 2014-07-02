from django.db import models


class ProjectReport(models.Model):
    name = models.CharField(max_length=10, default='')

    def __unicode__(self):
        return self.name 


class TestFTP(models.Model):
    name = models.CharField(max_length=10, default='')
    file_address = models.FileField(upload_to='files/')
    url = models.URLField(max_length=100)

    def __unicode__(self):
        return self.name 




