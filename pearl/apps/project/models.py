"""
Models for Project App.
"""

from django.contrib.auth.models import User
from django.db import models


STATUS_CODES = ((5, 'Uploading Files.'),
                (-6, 'Unable to upload files.'),
                (-7, 'Failed at Unicode check.'),
                (-11, 'Error at Quality check.'),
                (15, 'Review Quality.'),
                (20, 'Processing the files.'),
                (-21, 'Unable to process files.'),
                (25, 'Read Report.'),)


class NewProject(models.Model):
    customer = models.ForeignKey(User, related_name='original_customer_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    file_type = models.CharField(max_length=10)
    vcf_file1 = models.CharField(max_length=200, blank=True)
    total_fastq_files = models.SmallIntegerField(default=1,
                                                 blank=True,)
    fastq_file1 = models.CharField(max_length=200, blank=True)
    fastq_file2 = models.CharField(max_length=200, blank=True)
    file_list = models.CharField(max_length=200, blank=True)
    paired_end_distance = models.IntegerField(blank=True, null=True)
    tissue = models.CharField(max_length=100, default='', blank=True,
                              verbose_name='Tissue (Coming Soon)')
    disease = models.CharField(max_length=100, default='', blank=True,
                               verbose_name='Disease (Coming Soon)')
    status = models.IntegerField(choices=STATUS_CODES, default=5)
    start_processing = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name    # pragma: no cover

    class Meta:
        ordering = ('updated_at',)

    def save(self, *args, **kwargs):
        super(NewProject, self).save(*args, **kwargs)
        from apps.project.tasks import project_queue
        project_queue.apply_async(args=[self.pk, self.status, self.file_type],)


class MeshTissues(models.Model):
    descriptorui = models.CharField(max_length=7)
    descriptornamestring = models.CharField(max_length=41, blank=True)
    treenumber = models.TextField(blank=True)


class MeshDiseases(models.Model):
    descriptorui = models.CharField(max_length=7)
    descriptornamestring = models.CharField(max_length=100, blank=True)
    treenumber = models.TextField(blank=True)
