# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Zone'
        db.create_table('horta_zone', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Zone', max_length=100)),
        ))
        db.send_create_signal('horta', ['Zone'])

        # Adding model 'PolygonRepresentation'
        db.create_table('horta_polygonrepresentation', (
            ('georepresentation_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.GeoRepresentation'], unique=True, primary_key=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
        ))
        db.send_create_signal('horta', ['PolygonRepresentation'])

        # Adding model 'Canteiro'
        db.create_table('horta_canteiro', (
            ('zone_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Zone'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('horta', ['Canteiro'])

        # Adding model 'Item'
        db.create_table('horta_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('horta', ['Item'])

        # Adding model 'GeoRepresentation'
        db.create_table('horta_georepresentation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Item'])),
        ))
        db.send_create_signal('horta', ['GeoRepresentation'])


    def backwards(self, orm):
        # Deleting model 'Zone'
        db.delete_table('horta_zone')

        # Deleting model 'PolygonRepresentation'
        db.delete_table('horta_polygonrepresentation')

        # Deleting model 'Canteiro'
        db.delete_table('horta_canteiro')

        # Deleting model 'Item'
        db.delete_table('horta_item')

        # Deleting model 'GeoRepresentation'
        db.delete_table('horta_georepresentation')


    models = {
        'horta.canteiro': {
            'Meta': {'object_name': 'Canteiro', '_ormbases': ['horta.Zone']},
            'zone_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Zone']", 'unique': 'True', 'primary_key': 'True'})
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
        'horta.polygonrepresentation': {
            'Meta': {'object_name': 'PolygonRepresentation', '_ormbases': ['horta.GeoRepresentation']},
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'georepresentation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.GeoRepresentation']", 'unique': 'True', 'primary_key': 'True'})
        },
        'horta.zone': {
            'Meta': {'object_name': 'Zone', '_ormbases': ['horta.Item']},
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Zone'", 'max_length': '100'})
        }
    }

    complete_apps = ['horta']