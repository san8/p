# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TestFTP.url'
        db.add_column(u'experiment_testftp', 'url',
                      self.gf('django.db.models.fields.URLField')(default='old', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TestFTP.url'
        db.delete_column(u'experiment_testftp', 'url')


    models = {
        u'experiment.projectreport': {
            'Meta': {'object_name': 'ProjectReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        u'experiment.testftp': {
            'Meta': {'object_name': 'TestFTP'},
            'file_address': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['experiment']