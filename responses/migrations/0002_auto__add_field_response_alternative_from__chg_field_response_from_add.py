# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Response.alternative_from'
        db.add_column(u'responses_response', 'alternative_from',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Response.from_address'
        db.alter_column(u'responses_response', 'from_address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['responses.FromAddress'], null=True))

    def backwards(self, orm):
        # Deleting field 'Response.alternative_from'
        db.delete_column(u'responses_response', 'alternative_from')


        # Changing field 'Response.from_address'
        db.alter_column(u'responses_response', 'from_address_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['responses.FromAddress']))

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
            'alternative_from': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'from_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['responses.FromAddress']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['responses']