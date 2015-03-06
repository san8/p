# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeshDiseases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descriptorui', models.CharField(max_length=7)),
                ('descriptornamestring', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeshTissues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descriptorui', models.CharField(max_length=7)),
                ('descriptornamestring', models.CharField(max_length=41, blank=True)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Project Name')),
                ('description', models.CharField(max_length=100, null=True, verbose_name=b'Project Description', blank=True)),
                ('file_type', models.CharField(max_length=10)),
                ('total_fastq_files', models.SmallIntegerField(default=1, blank=True)),
                ('fastq_file1', models.CharField(max_length=200, null=True, blank=True)),
                ('fastq_file2', models.CharField(max_length=200, null=True, blank=True)),
                ('vcf_upload_type', models.SmallIntegerField(default=3, blank=True)),
                ('vcf_file1', models.CharField(max_length=200, blank=True)),
                ('vcf_file', models.FileField(upload_to=b'Project/', blank=True)),
                ('paired_end_distance', models.IntegerField(default=0, blank=True)),
                ('tissue', models.CharField(max_length=100, null=True, verbose_name=b'Tissue (Coming Soon)', blank=True)),
                ('disease', models.CharField(help_text=b'\n    <a href="http://www.nlm.nih.gov/mesh/MBrowser.html" target="_blank">\n    Disease Mesh Terms\n    </a>', max_length=100, null=True, verbose_name=b'Disease', blank=True)),
                ('status', models.IntegerField(default=5, choices=[(5, b'Uploading Files.'), (-6, b'Unable to upload files.'), (-7, b'Failed at Unicode check.'), (-11, b'Error at Quality check.'), (15, b'Review Quality.'), (20, b'Processing the files.'), (-21, b'Unable to process files.'), (25, b'Read Report.')])),
                ('start_processing', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('updated_at',),
                'get_latest_by': 'id',
            },
            bases=(models.Model,),
        ),
    ]
