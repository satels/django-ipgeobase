# coding: utf-8
from django.conf import settings

IPGEOBASE_SOURCE_URL = getattr(settings, 'IPGEOBASE_SOURCE_URL', 'http://ipgeobase.ru/files/db/Main/geo_files.zip')
IPGEOBASE_CODING = getattr(settings, 'IPGEOBASE_CODING', 'windows-1251')
IPGEOBASE_SEND_MESSAGE_FOR_ERRORS = getattr(settings, 'IPGEOBASE_SEND_MESSAGE_FOR_ERRORS', True)
