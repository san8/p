"""
Models for Project App.
"""

from django.contrib.auth.models import User
from django.db import models


UPLOADING_FILES = 0
CHECKING_QUALITY, FTP_FAILED = 1, -1
APPROVAL_WAITING, QC_FAILED = 2, -2
PROCESSING, APPROVAL_FAILED = 3, -3
REPORT, PROCESSING_FAILED = 4, -4

STATUS_OPTIONS = (
    (UPLOADING_FILES, 'Uploading Files.'),
    (CHECKING_QUALITY, 'Checking Quality.'),
    (APPROVAL_WAITING, 'Review Quality.'),
    (PROCESSING, 'Processing the file.'),
    (REPORT, 'Read Report.'),

    (FTP_FAILED, 'Unable to upload files.'),
    (QC_FAILED, 'Error at Quality check.'),
    (APPROVAL_FAILED, 'Project terminated at QC.'),
    (PROCESSING_FAILED, 'Unable to process files.'),
)


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
    status = models.IntegerField(choices=STATUS_OPTIONS, default=UPLOADING_FILES)
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
