# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customers'
        db.create_table(u'home_customers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=100)),
            ('new_field', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'home', ['Customers'])


    def backwards(self, orm):
        # Deleting model 'Customers'
        db.delete_table(u'home_customers')


    models = {
        u'home.customers': {
            'Meta': {'object_name': 'Customers'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'new_field': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['home']