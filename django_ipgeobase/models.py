#encoding:utf-8
from django.db import models
from django_ipgeobase.managers import IPGeoBaseManager


class IPGeoBase(models.Model):
    """Таблица перечень блоков ip-адресов с координатами"""
    
    ip_block = models.CharField(u'Блок IP-адресов',
        max_length=64, help_text=(
            u"Данное поле состоит из начального и конечного адресов блока, "
            u"отделенных друг от друга пробелом, тире и пробелом"
        ),
    )
    start_ip = models.BigIntegerField(
        u'Начальный IP-адрес блока, преобразованный в число',
        db_index=True, help_text=(
            u"IP-адрес иммет вид a.b.c.d, где a-d числа в диапазоне 0-255. "
            u"Преобразование в число происходит по формуле 256³*a+256²*b+256*c+d"
        ),
    )
    end_ip = models.BigIntegerField(
        u'Конечный IP-адрес блока, преобразованный в число',
        db_index=True
    )
    city = models.CharField(u'Город',
        max_length=255, null=True, help_text=(
            u"Данное поле содержит в себе название города, соответствующего "
            u"данному блоку"
        ),
    )
    region = models.CharField(u'Регион',
        max_length=255, null=True, help_text=(
            u"Данное поле содержит в себе название региона, соответствующего "
            u"данному блоку"
        ),
    )
    district = models.CharField(u'Округ',
        max_length=255, null=True, help_text=(
            u"Данное поле содержит в себе название федерального округа, "
            u"соответствующего данному блоку IP-адресов"
        ),
    )
    latitude = models.FloatField(u'Широта', null=True)
    longitude = models.FloatField(u'Долгота', null=True)
    country = models.CharField(u'Страна', max_length=16)

    objects = IPGeoBaseManager()

    class Meta:
        unique_together = [
            ('start_ip', 'end_ip'),
        ]