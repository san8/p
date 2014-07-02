# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectReport'
        db.create_table(u'experiment_projectreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
        ))
        db.send_create_signal(u'experiment', ['ProjectReport'])


    def backwards(self, orm):
        # Deleting model 'ProjectReport'
        db.delete_table(u'experiment_projectreport')


    models = {
        u'experiment.projectreport': {
            'Meta': {'object_name': 'ProjectReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        }
    }

    complete_apps = ['experiment']