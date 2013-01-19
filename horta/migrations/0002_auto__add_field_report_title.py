# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Report.title'
        db.add_column('horta_report', 'title',
                      self.gf('django.db.models.fields.CharField')(default='report', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Report.title'
        db.delete_column('horta_report', 'title')


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
            'scientific_name': ('django.db.models.fields.CharField', [], {'default': "'unspecified'", 'max_length': '100'})
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