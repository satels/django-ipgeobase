#!/usr/bin/env python
# coding: utf-8
from distutils.core import setup

import sys

is_py2 = sys.version_info < (3, 0, 0)

if is_py2:
    reload(sys).setdefaultencoding("UTF-8")

long_description = open('README.rst').read()

if is_py2:
    long_description = long_description.decode('utf8')

setup(
    name='django-ipgeobase',
    version='1.0.6',
    author='Ivan Petukhov',
    author_email='satels@gmail.com',
    packages=['django_ipgeobase', 'django_ipgeobase.management',
              'django_ipgeobase.management.commands',
              'django_ipgeobase.migrations'],
    url='https://github.com/satels/django-ipgeobase',
    download_url='https://github.com/satels/django-ipgeobase/zipball/master',
    license='MIT license',
    description='Приложение для работы с базой ipgeobase.ru.'.encode('utf8'),
    long_description=long_description,

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
