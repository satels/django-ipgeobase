# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django_ipgeobase.managers import IPGeoBaseManager


class IPGeoBase(models.Model):
    """Таблица перечень блоков ip-адресов с координатами"""

    ip_block = models.CharField(
        verbose_name='Блок IP-адресов',
        max_length=64,
        help_text=(
            "Данное поле состоит из начального и конечного адресов блока, "
            "отделенных друг от друга пробелом, тире и пробелом"
        ),
    )
    start_ip = models.BigIntegerField(
        verbose_name='Начальный IP-адрес блока, преобразованный в число',
        db_index=True,
        help_text=(
            "IP-адрес иммет вид a.b.c.d, где a-d числа в диапазоне 0-255. "
            "Преобразование в число происходит по формуле 256³*a+256²*b+256*c+d"
        ),
    )
    end_ip = models.BigIntegerField(
        verbose_name='Конечный IP-адрес блока, преобразованный в число',
        db_index=True,
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=255,
        null=True,
        db_index=True,
        help_text=(
            "Данное поле содержит в себе название города, соответствующего "
            "данному блоку"
        ),
    )
    city_id = models.IntegerField(
        verbose_name='Ipgeobase Id Города',
        null=True,
        help_text="Внутренний Ipgeobase Id Города",
    )
    region = models.CharField(
        verbose_name='Регион',
        max_length=255,
        null=True,
        help_text=(
            "Данное поле содержит в себе название региона, соответствующего "
            "данному блоку"
        ),
    )
    district = models.CharField(
        verbose_name='Округ',
        max_length=255,
        null=True,
        help_text=(
            "Данное поле содержит в себе название федерального округа, "
            "соответствующего данному блоку IP-адресов"
        ),
    )
    latitude = models.FloatField(verbose_name='Широта', null=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True)
    country = models.CharField(verbose_name='Страна', max_length=16)

    objects = IPGeoBaseManager()

    class Meta:
        index_together = [
            ('start_ip', 'end_ip'),
        ]
        unique_together = [
            ('start_ip', 'end_ip'),
        ]
