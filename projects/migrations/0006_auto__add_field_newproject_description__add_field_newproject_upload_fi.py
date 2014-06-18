# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewProject.description'
        db.add_column(u'projects_newproject', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'NewProject.upload_file'
        db.add_column(u'projects_newproject', 'upload_file',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'NewProject.ftp_file'
        db.add_column(u'projects_newproject', 'ftp_file',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'NewProject.tissue'
        db.add_column(u'projects_newproject', 'tissue',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'NewProject.disease'
        db.add_column(u'projects_newproject', 'disease',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewProject.description'
        db.delete_column(u'projects_newproject', 'description')

        # Deleting field 'NewProject.upload_file'
        db.delete_column(u'projects_newproject', 'upload_file')

        # Deleting field 'NewProject.ftp_file'
        db.delete_column(u'projects_newproject', 'ftp_file')

        # Deleting field 'NewProject.tissue'
        db.delete_column(u'projects_newproject', 'tissue')

        # Deleting field 'NewProject.disease'
        db.delete_column(u'projects_newproject', 'disease')


    models = {
        u'projects.newproject': {
            'Meta': {'object_name': 'NewProject'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'disease': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'ftp_file': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'optional': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'tissue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['projects']