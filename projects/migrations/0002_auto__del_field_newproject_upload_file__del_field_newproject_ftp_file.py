# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NewProject.upload_file'
        db.delete_column(u'projects_newproject', 'upload_file')

        # Deleting field 'NewProject.ftp_file'
        db.delete_column(u'projects_newproject', 'ftp_file')


    def backwards(self, orm):
        # Adding field 'NewProject.upload_file'
        db.add_column(u'projects_newproject', 'upload_file',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'NewProject.ftp_file'
        db.add_column(u'projects_newproject', 'ftp_file',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=50),
                      keep_default=False)


    models = {
        u'projects.newproject': {
            'Meta': {'object_name': 'NewProject'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'disease': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tissue': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['projects']