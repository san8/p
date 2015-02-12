# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewProject'
        db.create_table(u'project_newproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='original_customer_id', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('file_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('total_fastq_files', self.gf('django.db.models.fields.SmallIntegerField')(default=1, blank=True)),
            ('fastq_file1', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fastq_file2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('vcf_upload_type', self.gf('django.db.models.fields.SmallIntegerField')(default=3, blank=True)),
            ('vcf_file1', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('vcf_file', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100)),
            ('paired_end_distance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tissue', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('disease', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('start_processing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'project', ['NewProject'])


    def backwards(self, orm):
        # Deleting model 'NewProject'
        db.delete_table(u'project_newproject')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.meshdiseases': {
            'Meta': {'object_name': 'MeshDiseases', 'managed': 'False'},
            'descriptornamestring': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'descriptorui': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'project.meshtissues': {
            'Meta': {'object_name': 'MeshTissues', 'managed': 'False'},
            'descriptornamestring': ('django.db.models.fields.CharField', [], {'max_length': '41', 'blank': 'True'}),
            'descriptorui': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'project.newproject': {
            'Meta': {'ordering': "('updated_at',)", 'object_name': 'NewProject'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'original_customer_id'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'disease': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'fastq_file1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fastq_file2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paired_end_distance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_processing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'tissue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'total_fastq_files': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vcf_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'vcf_file1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'vcf_upload_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '3', 'blank': 'True'})
        }
    }

    complete_apps = ['project']