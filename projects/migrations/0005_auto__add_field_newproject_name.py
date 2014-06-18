# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewProject.name'
        db.add_column(u'projects_newproject', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewProject.name'
        db.delete_column(u'projects_newproject', 'name')


    models = {
        u'projects.newproject': {
            'Meta': {'object_name': 'NewProject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'optional': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['projects']