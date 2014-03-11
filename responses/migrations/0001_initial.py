# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FromAddress'
        db.create_table(u'responses_fromaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'responses', ['FromAddress'])

        # Adding model 'Response'
        db.create_table(u'responses_response', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['responses.FromAddress'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'responses', ['Response'])

        # Adding model 'Destination'
        db.create_table(u'responses_destination', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('response', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['responses.Response'])),
            ('send_type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'responses', ['Destination'])


    def backwards(self, orm):
        # Deleting model 'FromAddress'
        db.delete_table(u'responses_fromaddress')

        # Deleting model 'Response'
        db.delete_table(u'responses_response')

        # Deleting model 'Destination'
        db.delete_table(u'responses_destination')


    models = {
        u'responses.destination': {
            'Meta': {'object_name': 'Destination'},
            'address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'response': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.Response']"}),
            'send_type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'responses.fromaddress': {
            'Meta': {'object_name': 'FromAddress'},
            'address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'responses.response': {
            'Meta': {'object_name': 'Response'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'from_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.FromAddress']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['responses']