#encoding: utf-8
from django.conf import settings

#Путь до файла block_coord.db
IPGEOBASE_SOURCE_URL = getattr(settings, 'IPGEOBASE_SOURCE_URL', 'http://ipgeobase.ru/files/db/Map_db/block_coord.zip')
IPGEOBASE_FILENAME = getattr(settings, 'IPGEOBASE_FILENAME', "block_coord.db")
IPGEOBASE_CODING = getattr(settings, 'IPGEOBASE_CODING', 'windows-1251')
IPGEOBASE_SEND_MESSAGE_FOR_ERRORS = getattr(settings, 'IPGEOBASE_SEND_MESSAGE_FOR_ERRORS', True)