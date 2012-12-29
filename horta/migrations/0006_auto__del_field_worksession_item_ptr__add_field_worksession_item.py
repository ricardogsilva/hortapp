# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'WorkSession.item_ptr'
        db.delete_column('horta_worksession', 'item_ptr_id')

        # Adding field 'WorkSession.item'
        db.add_column('horta_worksession', 'item',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['horta.Item'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'WorkSession.item_ptr'
        raise RuntimeError("Cannot reverse this migration. 'WorkSession.item_ptr' and its values cannot be restored.")
        # Deleting field 'WorkSession.item'
        db.delete_column('horta_worksession', 'item_id')


    models = {
        'horta.bed': {
            'Meta': {'object_name': 'Bed', '_ormbases': ['horta.Zone']},
            'zone': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Zone']", 'unique': 'True', 'primary_key': 'True'})
        },
        'horta.garden': {
            'Meta': {'object_name': 'Garden', '_ormbases': ['horta.Item']},
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horta.georepresentation': {
            'Meta': {'object_name': 'GeoRepresentation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Item']"})
        },
        'horta.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'horta.parcel': {
            'Meta': {'object_name': 'Parcel', '_ormbases': ['horta.Item']},
            'garden': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Garden']"}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Parcel'", 'max_length': '100'})
        },
        'horta.plantation': {
            'Meta': {'object_name': 'Plantation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Species']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Zone']"})
        },
        'horta.polygonrepresentation': {
            'Meta': {'object_name': 'PolygonRepresentation', '_ormbases': ['horta.GeoRepresentation']},
            'geo_representation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.GeoRepresentation']", 'unique': 'True', 'primary_key': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {})
        },
        'horta.species': {
            'Meta': {'object_name': 'Species', '_ormbases': ['horta.Item']},
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unspecified'", 'max_length': '100'})
        },
        'horta.worksession': {
            'Meta': {'object_name': 'WorkSession', '_ormbases': ['horta.Item']},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'garden': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Garden']"}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'})
        },
        'horta.zone': {
            'Meta': {'object_name': 'Zone', '_ormbases': ['horta.Item']},
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Zone'", 'max_length': '100'}),
            'parcel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Parcel']"})
        }
    }

    complete_apps = ['horta']