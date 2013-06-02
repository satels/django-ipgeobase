# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IPGeoBase'
        db.create_table(u'django_ipgeobase_ipgeobase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_block', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('start_ip', self.gf('django.db.models.fields.BigIntegerField')(db_index=True)),
            ('end_ip', self.gf('django.db.models.fields.BigIntegerField')(db_index=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, db_index=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'django_ipgeobase', ['IPGeoBase'])

        # Adding unique constraint on 'IPGeoBase', fields ['start_ip', 'end_ip']
        db.create_unique(u'django_ipgeobase_ipgeobase', ['start_ip', 'end_ip'])


    def backwards(self, orm):
        # Removing unique constraint on 'IPGeoBase', fields ['start_ip', 'end_ip']
        db.delete_unique(u'django_ipgeobase_ipgeobase', ['start_ip', 'end_ip'])

        # Deleting model 'IPGeoBase'
        db.delete_table(u'django_ipgeobase_ipgeobase')


    models = {
        u'django_ipgeobase.ipgeobase': {
            'Meta': {'unique_together': "[('start_ip', 'end_ip')]", 'object_name': 'IPGeoBase'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'end_ip': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_block': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'start_ip': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['django_ipgeobase']