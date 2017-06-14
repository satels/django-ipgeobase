# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

try:
    from django.db import migrations  # Django >= 1.7

    class Migration(migrations.Migration):

        initial = True

        dependencies = [
        ]

        operations = [
            migrations.CreateModel(
                name='IPGeoBase',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('ip_block', models.CharField(help_text='Данное поле состоит из начального и конечного адресов блока, отделенных друг от друга пробелом, тире и пробелом', max_length=64, verbose_name='Блок IP-адресов')),
                    ('start_ip', models.BigIntegerField(db_index=True, help_text='IP-адрес иммет вид a.b.c.d, где a-d числа в диапазоне 0-255. Преобразование в число происходит по формуле 256³*a+256²*b+256*c+d', verbose_name='Начальный IP-адрес блока, преобразованный в число')),
                    ('end_ip', models.BigIntegerField(db_index=True, verbose_name='Конечный IP-адрес блока, преобразованный в число')),
                    ('city', models.CharField(db_index=True, help_text='Данное поле содержит в себе название города, соответствующего данному блоку', max_length=255, null=True, verbose_name='Город')),
                    ('region', models.CharField(help_text='Данное поле содержит в себе название региона, соответствующего данному блоку', max_length=255, null=True, verbose_name='Регион')),
                    ('district', models.CharField(help_text='Данное поле содержит в себе название федерального округа, соответствующего данному блоку IP-адресов', max_length=255, null=True, verbose_name='Округ')),
                    ('latitude', models.FloatField(null=True, verbose_name='Широта')),
                    ('longitude', models.FloatField(null=True, verbose_name='Долгота')),
                    ('country', models.CharField(max_length=16, verbose_name='Страна')),
                ],
            ),
            migrations.AlterUniqueTogether(
                name='ipgeobase',
                unique_together=set([('start_ip', 'end_ip')]),
            ),
        ]

except ImportError:
    # Django < 1.7
    from south.db import db
    from south.v2 import SchemaMigration


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
