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
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True)),
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
            ('scientific_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
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

        # Adding model 'Meeting'
        db.create_table('horta_meeting', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('horta', ['Meeting'])

        # Adding M2M table for field users on 'Meeting'
        db.create_table('horta_meeting_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meeting', models.ForeignKey(orm['horta.meeting'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('horta_meeting_users', ['meeting_id', 'user_id'])

        # Adding model 'WorkSession'
        db.create_table('horta_worksession', (
            ('meeting_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Meeting'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('horta', ['WorkSession'])

        # Adding M2M table for field zones on 'WorkSession'
        db.create_table('horta_worksession_zones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('worksession', models.ForeignKey(orm['horta.worksession'], null=False)),
            ('zone', models.ForeignKey(orm['horta.zone'], null=False))
        ))
        db.create_unique('horta_worksession_zones', ['worksession_id', 'zone_id'])

        # Adding model 'Report'
        db.create_table('horta_report', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('worksession', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['horta.WorkSession'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('horta', ['Report'])

        # Adding model 'Task'
        db.create_table('horta_task', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['horta.Item'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='task_author', to=orm['auth.User'])),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('horta', ['Task'])

        # Adding M2M table for field zones on 'Task'
        db.create_table('horta_task_zones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm['horta.task'], null=False)),
            ('zone', models.ForeignKey(orm['horta.zone'], null=False))
        ))
        db.create_unique('horta_task_zones', ['task_id', 'zone_id'])


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

        # Deleting model 'Meeting'
        db.delete_table('horta_meeting')

        # Removing M2M table for field users on 'Meeting'
        db.delete_table('horta_meeting_users')

        # Deleting model 'WorkSession'
        db.delete_table('horta_worksession')

        # Removing M2M table for field zones on 'WorkSession'
        db.delete_table('horta_worksession_zones')

        # Deleting model 'Report'
        db.delete_table('horta_report')

        # Deleting model 'Task'
        db.delete_table('horta_task')

        # Removing M2M table for field zones on 'Task'
        db.delete_table('horta_task_zones')


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
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
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
        'horta.meeting': {
            'Meta': {'object_name': 'Meeting', '_ormbases': ['horta.Item']},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
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
        'horta.report': {
            'Meta': {'object_name': 'Report', '_ormbases': ['horta.Item']},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'worksession': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['horta.WorkSession']"})
        },
        'horta.species': {
            'Meta': {'object_name': 'Species', '_ormbases': ['horta.Item']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unspecified'", 'max_length': '100'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'horta.task': {
            'Meta': {'object_name': 'Task', '_ormbases': ['horta.Item']},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_author'", 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zones': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['horta.Zone']", 'null': 'True', 'blank': 'True'})
        },
        'horta.worksession': {
            'Meta': {'object_name': 'WorkSession', '_ormbases': ['horta.Meeting']},
            'meeting_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['horta.Meeting']", 'unique': 'True', 'primary_key': 'True'}),
            'zones': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['horta.Zone']", 'null': 'True', 'blank': 'True'})
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