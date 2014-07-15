from django.contrib.auth.models import User 
from django.db import models

from .tasks import project_created 


TISSUE_CHOICES = (
    ('Tissue_A', 'TISSUE_A'),
    ('Tissue_B', 'TISSUE_B'),
)
DISEASE_CHOICES = (
    ('Disease A', 'Disease A'),
    ('Disease B', 'Disease B'),
)

class NewProject(models.Model):
    customer = models.ForeignKey(User, related_name='original_customer_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    file_type = models.CharField(max_length=10)
    vcf_file1 = models.URLField(max_length=200, blank=True)
    total_fastq_files = models.SmallIntegerField(default=0, 
                                                 blank=True, 
                                                 null=True,)
    fastq_file1 = models.URLField(max_length=200, blank=True)
    fastq_file2 = models.URLField(max_length=200, blank=True)
    paired_end_distance = models.IntegerField(blank=True, null=True)
    tissue = models.CharField(max_length=30, default='',
            choices=TISSUE_CHOICES,)
    disease = models.CharField(max_length=100, default='',
            choices=DISEASE_CHOICES,)
    status = models.CharField(max_length=20, default='Raw Files Uploaded',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} : {}".format(self.customer.username, self.name)

    class Meta:
        ordering = ['updated_at']
        permissions = (
            ('view_report', 'view_report'),
        )

    def save(self, *args, **kwargs):
        super(NewProject, self).save(*args, **kwargs)
        project_created.apply_async(args=[self.pk,])


class ProjectReport(models.Model):
    project = models.ForeignKey(NewProject, related_name='project_as_foreign_key')
    pdf_file = models.CharField(max_length=100, default='')
    data = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return self.project.name 


