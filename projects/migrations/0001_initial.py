# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewProject'
        db.create_table(u'projects_newproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('upload_file', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100)),
            ('ftp_file', self.gf('django.db.models.fields.URLField')(default='', max_length=50)),
            ('tissue', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('disease', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'projects', ['NewProject'])


    def backwards(self, orm):
        # Deleting model 'NewProject'
        db.delete_table(u'projects_newproject')


    models = {
        u'projects.newproject': {
            'Meta': {'object_name': 'NewProject'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'disease': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ftp_file': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tissue': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['projects']