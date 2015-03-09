"""
Models for Project App.
"""
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


STATUS_CODES = ((5, 'Uploading Files.'),
                (-6, 'Unable to upload files.'),
                (-7, 'Failed at Unicode check.'),
                (-11, 'Error at Quality check.'),
                (15, 'Review Quality.'),
                (20, 'Processing the files.'),
                (-21, 'Unable to process files.'),
                (22, 'Processing Validation.'),
                (25, 'Read Report.'),)

FILE_TYPE_CHOICES = (('fastq', 'FASTQ'),
                     ('vcf', 'VCF'),)

NUMBER_OF_FASTQ = ((1, 'Single End'),
                   (2, 'Paired End'))

VCF_UPLOAD_CHOICES = ((3, 'FTP Upload'),
                      (4, 'Direct Upload'))

PROCESSING_CHOICES = ((1, 'Yes'),
                      (0, 'No'))


class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects')
    name = models.CharField(max_length=100, verbose_name='Project Name')
    description = models.CharField(max_length=100, blank=True, null=True,
                                   verbose_name="Project Description")
    file_type = models.CharField(max_length=10)
    total_fastq_files = models.SmallIntegerField(default=1,
                                                 blank=True)
    fastq_file1 = models.CharField(max_length=200, blank=True, null=True)
    fastq_file2 = models.CharField(max_length=200, blank=True, null=True)
    vcf_upload_type = models.SmallIntegerField(blank=True, default=3)
    vcf_file1 = models.CharField(max_length=200, blank=True)
    vcf_file = models.FileField(upload_to=settings.PROJECTS_PATH,
                                blank=True)
    paired_end_distance = models.IntegerField(blank=True, default=0)
    tissue = models.CharField(max_length=100, blank=True, null=True,
                              verbose_name='Tissue (Coming Soon)')
    disease = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name='Disease',
                               help_text='''
    <a href="http://www.nlm.nih.gov/mesh/MBrowser.html" target="_blank">
    Disease Mesh Terms
    </a>''')
    status = models.IntegerField(choices=STATUS_CODES, default=5)
    start_processing = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True,
                                      default=datetime.datetime.now)

    def __unicode__(self):
        return self.name    # pragma: no cover

    class Meta:
        ordering = ('updated_at',)
        get_latest_by = "id"

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        from apps.project.tasks import project_queue
        project_queue.apply_async(args=[self.pk, self.status, self.file_type],)


class MeshTissues(models.Model):
    """
    Table for mesh tissues.
    """
    descriptorui = models.CharField(max_length=7)
    descriptornamestring = models.CharField(max_length=41, blank=True)

    class Meta:
        managed = False

    def __unicode__(self):
        return self.descriptornamestring


class MeshDiseases(models.Model):
    """
    Table for mesh diseases.
    """
    descriptorui = models.CharField(max_length=7)
    descriptornamestring = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False

    def __unicode__(self):
        return self.descriptornamestring
