#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup

import sys
reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-ipgeobase',
    version='1.0.0-beta',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=['django_ipgeobase', 'django_ipgeobase.management',
              'django_ipgeobase.management.commands'],
    url='https://github.com/satels/django-ipgeobase',
    download_url = 'https://github.com/satels/django-ipgeobase/zipball/master',
    license = 'MIT license',
    description = u'Приложение для работы с базой ipgeobase.ru.'.encode('utf8'),
    long_description = open('README.rst').read().decode('utf8'),

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
