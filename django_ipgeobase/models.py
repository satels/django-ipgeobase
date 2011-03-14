#encoding:utf8
from django.db import models
from django_ipgeobase.managers import IPGeoBaseManager

class IPGeoBase(models.Model):
    """Таблица перечень блоков ip-адресов с координатами"""
    ip_block = models.CharField(u'Блок IP-адресов',
                                help_text=u"""Данное поле состоит из начального и конечного адресов блока, отделенных друг от друга пробелом, тире и пробелом""",
                                max_length=64)
    start_ip = models.BigIntegerField(u'Начальный IP-адрес блока, преобразованный в число',
                                      help_text=u"""IP-адрес иммет вид a.b.c.d, где a-d числа в диапазоне 0-255. Преобразование в число происходит по формуле 256³*a+256²*b+256*c+d""",
                                      db_index=True)
    end_ip = models.BigIntegerField(u'Конечный IP-адрес блока, преобразованный в число',
                                    db_index=True)
    city = models.CharField(u'Город',
                            help_text=u"""Данное поле содержит в себе название города, соответствующего данному блоку""",
                            max_length=255)
    region = models.CharField(u'Регион',
                              help_text=u"""Данное поле содержит в себе название региона, соответствующего данному блоку""",
                              max_length=255)
    district = models.CharField(u'Округ',
                                help_text=u"""Данное поле содержит в себе название федерального округа, соответствующего данному блоку IP-адресов""",
                                max_length=255)
    latitude = models.FloatField(u'Широта')
    longitude = models.FloatField(u'Долгота')

    objects = IPGeoBaseManager()
