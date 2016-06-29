# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('send_type', models.CharField(max_length=5, choices=[(b'to', b'To'), (b'cc', b'Cc'), (b'bcc', b'Bcc')])),
                ('address', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FromAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=255)),
                ('alternative_from', models.CharField(max_length=255, null=True, blank=True)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('from_address', models.ForeignKey(verbose_name=b'From', blank=True, to='responses.FromAddress', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='destination',
            name='response',
            field=models.ForeignKey(to='responses.Response'),
            preserve_default=True,
        ),
    ]
