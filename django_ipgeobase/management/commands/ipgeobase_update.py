#encoding:utf8
from django.core.management.base import NoArgsCommand
from django.db import connection, transaction
from django_ipgeobase.conf import *
from zipfile import ZipFile
from urllib import urlopen
from cStringIO import StringIO
from django.core.mail import mail_admins

DELETE_SQL = \
"""
DELETE FROM django_ipgeobase_ipgeobase
"""

INSERT_SQL = \
"""
INSERT INTO django_ipgeobase_ipgeobase
(ip_block, "start_ip", "end_ip", city, region, district, latitude, longitude)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

ERROR_SUBJECT = u"Error of command ipgeobase_update"
send_message = IPGEOBASE_SEND_MESSAGE_FOR_ERRORS

class Command(NoArgsCommand):

    def handle(self, *args, **options):
        print "Download zip-archive..."
        f = urlopen(IPGEOBASE_SOURCE_URL)
        buffer = StringIO(f.read())
        f.close()
        print "Unpacking..."
        zip_file = ZipFile(buffer)
        try:
            file_read = zip_file.read(IPGEOBASE_FILENAME)
        except KeyError:
            message = "File %s in archive not found" % IPGEOBASE_FILENAME
            if send_message:
                mail_admins(subject=ERROR_SUBJECT, message=message)
            return message
        zip_file.close()
        buffer.close()
        print "Start updating..."
        lines = file_read.decode(IPGEOBASE_CODING).split('\n')
        cursor = connection.cursor()
        transaction.enter_transaction_management()
        try:
            transaction.managed(True)
            print "Delete old rows in table ipgeobase..."
            cursor.execute(DELETE_SQL)
            print "Write new data..."
            cursor.executemany(INSERT_SQL,
                               [l.split('\t') for l in lines if l.strip()])
            transaction.commit()
        except Exception, e:
            message = "The data not updated:", e
            if send_message:
                mail_admins(subject=ERROR_SUBJECT, message=message)
            return message
        finally:
            transaction.rollback()
            transaction.leave_transaction_management()
        return "Table ipgeobase is update.\n"
