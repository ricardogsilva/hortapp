# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Media'
        db.create_table('horta_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('the_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('horta', ['Media'])

        # Adding model 'Item'
        db.create_table('horta_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('horta', ['Item'])

        # Adding M2M table for field files on 'Item'
        db.create_table('horta_item_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm['horta.item'], null=False)),
            ('media', models.ForeignKey(orm['horta.media'], null=False))
        ))
        db.create_unique('horta_item_files', ['item_id', 'media_id'])

        # Adding model 'Garden'
        db.create_table('horta_garden', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True)),
        ))
        db.send_create_signal('horta', ['Garden'])

        # Adding model 'Parcel'
        db.create_table('horta_parcel', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('garden', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Garden'])),
            ('name', self.gf('django.db.models.fields.CharField')(default='Parcel', max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True)),
        ))
        db.send_create_signal('horta', ['Parcel'])

        # Adding model 'Zone'
        db.create_table('horta_zone', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('parcel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Parcel'])),
            ('name', self.gf('django.db.models.fields.CharField')(default='Zone', max_length=100)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
        ))
        db.send_create_signal('horta', ['Zone'])

        # Adding model 'Bed'
        db.create_table('horta_bed', (
            ('zone', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Zone'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('horta', ['Bed'])

        # Adding model 'Species'
        db.create_table('horta_species', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='unspecified', max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('horta', ['Species'])

        # Adding model 'Plantation'
        db.create_table('horta_plantation', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Species'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.Zone'])),
        ))
        db.send_create_signal('horta', ['Plantation'])

        # Adding model 'WorkSession'
        db.create_table('horta_worksession', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('horta', ['WorkSession'])

        # Adding M2M table for field zones on 'WorkSession'
        db.create_table('horta_worksession_zones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('worksession', models.ForeignKey(orm['horta.worksession'], null=False)),
            ('zone', models.ForeignKey(orm['horta.zone'], null=False))
        ))
        db.create_unique('horta_worksession_zones', ['worksession_id', 'zone_id'])

        # Adding M2M table for field users on 'WorkSession'
        db.create_table('horta_worksession_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('worksession', models.ForeignKey(orm['horta.worksession'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horta_worksession_users', ['worksession_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'Media'
        db.delete_table('horta_media')

        # Deleting model 'Item'
        db.delete_table('horta_item')

        # Removing M2M table for field files on 'Item'
        db.delete_table('horta_item_files')

        # Deleting model 'Garden'
        db.delete_table('horta_garden')

        # Deleting model 'Parcel'
        db.delete_table('horta_parcel')

        # Deleting model 'Zone'
        db.delete_table('horta_zone')

        # Deleting model 'Bed'
        db.delete_table('horta_bed')

        # Deleting model 'Species'
        db.delete_table('horta_species')

        # Deleting model 'Plantation'
        db.delete_table('horta_plantation')

        # Deleting model 'WorkSession'
        db.delete_table('horta_worksession')

        # Removing M2M table for field zones on 'WorkSession'
        db.delete_table('horta_worksession_zones')

        # Removing M2M table for field users on 'WorkSession'
        db.delete_table('horta_worksession_users')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horta.bed': {
            'Meta': {'object_name': 'Bed', '_ormbases': ['horta.Zone']},
            'zone': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Zone']", 'unique': 'True', 'primary_key': 'True'})
        },
        'horta.garden': {
            'Meta': {'object_name': 'Garden', '_ormbases': ['horta.Item']},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'horta.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['horta.Media']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'horta.media': {
            'Meta': {'object_name': 'Media'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'the_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'horta.parcel': {
            'Meta': {'object_name': 'Parcel', '_ormbases': ['horta.Item']},
            'garden': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Garden']"}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Parcel'", 'max_length': '100'})
        },
        'horta.plantation': {
            'Meta': {'object_name': 'Plantation', '_ormbases': ['horta.Item']},
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Species']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Zone']"})
        },
        'horta.species': {
            'Meta': {'object_name': 'Species', '_ormbases': ['horta.Item']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unspecified'", 'max_length': '100'})
        },
        'horta.worksession': {
            'Meta': {'object_name': 'WorkSession', '_ormbases': ['horta.Item']},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'zones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['horta.Zone']", 'symmetrical': 'False'})
        },
        'horta.zone': {
            'Meta': {'object_name': 'Zone', '_ormbases': ['horta.Item']},
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Zone'", 'max_length': '100'}),
            'parcel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.Parcel']"})
        }
    }

    complete_apps = ['horta']