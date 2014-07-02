# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Knight.of_the_round_table'
        db.delete_column(u'southtut_knight', 'of_the_round_table')

        # Deleting field 'Knight.name'
        db.delete_column(u'southtut_knight', 'name')

        # Deleting field 'Knight.wherever'
        db.delete_column(u'southtut_knight', 'wherever')

        # Deleting field 'Knight.dances_wherever'
        db.delete_column(u'southtut_knight', 'dances_wherever')

        # Adding field 'Knight.first_name'
        db.add_column(u'southtut_knight', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Knight.last_name'
        db.add_column(u'southtut_knight', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Knight.of_the_round_table'
        db.add_column(u'southtut_knight', 'of_the_round_table',
                      self.gf('django.db.models.fields.BooleanField')(default=datetime.datetime(2014, 6, 17, 0, 0)),
                      keep_default=False)

        # Adding field 'Knight.name'
        db.add_column(u'southtut_knight', 'name',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 6, 17, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'Knight.wherever'
        db.add_column(u'southtut_knight', 'wherever',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Knight.dances_wherever'
        db.add_column(u'southtut_knight', 'dances_wherever',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Knight.first_name'
        db.delete_column(u'southtut_knight', 'first_name')

        # Deleting field 'Knight.last_name'
        db.delete_column(u'southtut_knight', 'last_name')


    models = {
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['southtut']