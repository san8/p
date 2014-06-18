# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.wherever'
        db.add_column(u'southtut_knight', 'wherever',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.wherever'
        db.delete_column(u'southtut_knight', 'wherever')


    models = {
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'dances_wherever': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {}),
            'wherever': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['southtut']