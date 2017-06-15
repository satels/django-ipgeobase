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


Или версионированно ::

  $ pip install django-ipgeobase==1.0.5


Потом следует добавить 'django_ipgeobase' в INSTALLED_APPS и выполнить ::

  $ python manage.py syncdb  # Django < 1.7
  $ python manage.py migrate django_ipgeobase  # Django >= 1.7


Настройка
=========

Добавить app в settings.py ::

  INSTALLED_APPS = [
      ..
      'django_ipgeobase',
      ..
  ]

Необязательные параметры (в settings.py):

* IPGEOBASE_CODING - кодировка этого файла (по-умолчанию windows-1251, можно не менять).
* IPGEOBASE_SOURCE_URL - ссылка на этот файл на сайте-источнике (по-умолчанию установлено, можно не менять)
* IPGEOBASE_SEND_MESSAGE_FOR_ERRORS - отправлять ли сообщения об ошибках на почту при обновлении (по-умолчание, True)


Использование
=============

Для получения объекта ipgeobase (для определения региона) ::

  from __future__ import print_function, unicode_literals
  from django_ipgeobase.models import IPGeoBase

  ip = "212.49.98.48"

  ipgeobases = IPGeoBase.objects.by_ip(ip)
  if ipgeobases.exists():
      ipgeobase = ipgeobases[0]
      print(ipgeobase.country)  # 'RU' - Страна
      print(ipgeobase.district)  # Округ (для указанного ip - Уральский федеральный округ)
      print(ipgeobase.region)  # Регион (Свердловская область)
      print(ipgeobase.city)  # Населенный пункт (Екатеринбург)
      print(ipgeobase.ip_block)  # IP-блок, в который попали (212.49.96.0 - 212.49.127.255)
      print(ipgeobase.start_ip, ipgeobase.end_ip)  # (3560005632, 3560013823), IP-блок в числовом формате
      print(ipgeobase.latitude, ipgeobase.longitude)  # (56.837814, 60.596844), широта и долгота


Обновления базы
---------------

Чтобы обновить базу ipgeobase ::

  $ python manage.py ipgeobase_update
