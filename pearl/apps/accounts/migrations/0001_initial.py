# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0003_auto_20141117_1647'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salutation', models.CharField(max_length=10, blank=True)),
                ('company', models.CharField(max_length=50, blank=True)),
                ('phone_number', models.CharField(max_length=20, blank=True)),
                ('timezone', models.CharField(default=b'', max_length=50, blank=True)),
                ('balance', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(related_name='customer_to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fastq', models.FloatField(default=0.0)),
                ('vcf', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment', models.ForeignKey(related_name='paypal_id', to='ipn.PayPalIPN')),
                ('user', models.ForeignKey(related_name='payments_to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
