================
django-ipgeobase
================

django-ipgeobase - это приложение для определения региона (а также широты и долготы) в России по IP в Django

Установка
=========

Проделываем в командной строке ::

  $ git clone git://github.com/satels/django-ipgeobase.git
  $ cd django-ipgeobase
  $ python setup.py install


Потом следует добавить 'django_ipgeobase' в INSTALLED_APPS и выполнить ::

  $ python manage.py syncdb


Настройка
=========

Необязательные параметры (в settings.py):

* IPGEOBASE_CODING - кодировка этого файла (по-умолчанию windows-1251, можно не менять).
* IPGEOBASE_SOURCE_URL - ссылка на этот файл на сайте-источнике (по-умолчанию установлено, можно не менять)
* IPGEOBASE_SEND_MESSAGE_FOR_ERRORS - отправлять ли сообщения об ошибках на почту при обновлении (по-умолчание, True)


Использование
=============

Для получения объекта ipgeobase (для определения региона) ::

  from django_ipgeobase.models import IPGeoBase

  ip = "212.49.98.48"

  ipgeobases = IPGeoBase.objects.by_ip(ip)
  if ipgeobases.exists():
      ipgeobase = ipgeobases[0]
      print ipgeobase.country #Страна
      print ipgeobase.district #Округ (для указанного ip - Уральский)
      print ipgeobase.region #Регион (Свердловская область)
      print ipgeobase.city #Населенный пункт (Екатеринбург)
      print ipgeobase.ip_block #IP-блок, в который попали (212.49.98.0 - 212.49.98.255)
      print ipgeobase.start_ip, ipgeobase.end_ip #IP-блок в числовом формате
      print ipgeobase.latitude, ipgeobase.longitude #широта и долгота


Обновления базы
---------------

Чтобы обновить базу ipgeobase:

  $ python manage.py ipgeobase_update
