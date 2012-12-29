# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Canteiro'
        db.delete_table('horta_canteiro')

        # Deleting model 'Especie'
        db.delete_table('horta_especie')

        # Deleting model 'Plantacao'
        db.delete_table('horta_plantacao')

        # Adding model 'Plantation'
        db.create_table('horta_plantation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Species'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Zone'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('horta', ['Plantation'])

        # Adding model 'Bed'
        db.create_table('horta_bed', (
            ('zone', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Zone'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('horta', ['Bed'])

        # Adding model 'Species'
        db.create_table('horta_species', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='unspecified', max_length=100)),
        ))
        db.send_create_signal('horta', ['Species'])


    def backwards(self, orm):
        # Adding model 'Canteiro'
        db.create_table('horta_canteiro', (
            ('zone', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Zone'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('horta', ['Canteiro'])

        # Adding model 'Especie'
        db.create_table('horta_especie', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='unspecified', max_length=100)),
        ))
        db.send_create_signal('horta', ['Especie'])

        # Adding model 'Plantacao'
        db.create_table('horta_plantacao', (
            ('especie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Especie'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Zone'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('horta', ['Plantacao'])

        # Deleting model 'Plantation'
        db.delete_table('horta_plantation')

        # Deleting model 'Bed'
        db.delete_table('horta_bed')

        # Deleting model 'Species'
        db.delete_table('horta_species')


    models = {
        'horta.bed': {
            'Meta': {'object_name': 'Bed', '_ormbases': ['horta.Zone']},
            'zone': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Zone']", 'unique': 'True', 'primary_key': 'True'})
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
        'horta.zone': {
            'Meta': {'object_name': 'Zone', '_ormbases': ['horta.Item']},
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Zone'", 'max_length': '100'})
        }
    }

    complete_apps = ['horta']