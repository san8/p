# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topping'
        db.create_table(u'experiment_topping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'experiment', ['Topping'])

        # Adding model 'Pizza'
        db.create_table(u'experiment_pizza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'experiment', ['Pizza'])

        # Adding M2M table for field toppings on 'Pizza'
        m2m_table_name = db.shorten_name(u'experiment_pizza_toppings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pizza', models.ForeignKey(orm[u'experiment.pizza'], null=False)),
            ('topping', models.ForeignKey(orm[u'experiment.topping'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pizza_id', 'topping_id'])


    def backwards(self, orm):
        # Deleting model 'Topping'
        db.delete_table(u'experiment_topping')

        # Deleting model 'Pizza'
        db.delete_table(u'experiment_pizza')

        # Removing M2M table for field toppings on 'Pizza'
        db.delete_table(db.shorten_name(u'experiment_pizza_toppings'))


    models = {
        u'experiment.pizza': {
            'Meta': {'object_name': 'Pizza'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'toppings': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['experiment.Topping']", 'symmetrical': 'False'})
        },
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
        },
        u'experiment.topping': {
            'Meta': {'object_name': 'Topping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['experiment']