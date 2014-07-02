# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'django_celery_example_userprofile')


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'django_celery_example_userprofile', (
            ('token', self.gf('django.db.models.fields.CharField')(max_length=32)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='user_profile', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'django_celery_example', ['UserProfile'])


    models = {
        u'django_celery_example.samplecount': {
            'Meta': {'object_name': 'SampleCount'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['django_celery_example']