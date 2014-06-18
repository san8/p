# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NewProject.description'
        db.delete_column(u'projects_newproject', 'description')

        # Deleting field 'NewProject.tissue'
        db.delete_column(u'projects_newproject', 'tissue')

        # Deleting field 'NewProject.disease'
        db.delete_column(u'projects_newproject', 'disease')

        # Deleting field 'NewProject.name'
        db.delete_column(u'projects_newproject', 'name')


    def backwards(self, orm):
        # Adding field 'NewProject.description'
        db.add_column(u'projects_newproject', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'NewProject.tissue'
        db.add_column(u'projects_newproject', 'tissue',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'NewProject.disease'
        db.add_column(u'projects_newproject', 'disease',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'NewProject.name'
        db.add_column(u'projects_newproject', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    models = {
        u'projects.newproject': {
            'Meta': {'object_name': 'NewProject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optional': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['projects']