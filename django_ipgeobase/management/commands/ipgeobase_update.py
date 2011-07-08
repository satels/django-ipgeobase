#encoding:utf8
from cStringIO import StringIO
from django.core.mail import mail_admins
from django.core.management.base import NoArgsCommand, CommandError
from django.db import connection, transaction
from django_ipgeobase.conf import IPGEOBASE_SOURCE_URL, IPGEOBASE_CODING, \
    IPGEOBASE_SEND_MESSAGE_FOR_ERRORS
from urllib import urlopen
from zipfile import ZipFile

DELETE_SQL = "DELETE FROM django_ipgeobase_ipgeobase"

INSERT_SQL = """
INSERT INTO django_ipgeobase_ipgeobase
("start_ip", "end_ip", ip_block, country, city, region, district, latitude, longitude)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        cities_file_read = _read_file(zip_file, 'cities.txt')
        cidr_optim_file_read = _read_file(zip_file, 'cidr_optim.txt')
        zip_file.close()
        buffer.close()
        print "Start updating..."
        list_cities = cities_file_read.decode(IPGEOBASE_CODING).split('\n')
        list_cidr_optim = \
            cidr_optim_file_read.decode(IPGEOBASE_CODING).split('\n')
        lines = \
            _get_cidr_optim_with_cities_lines(list_cidr_optim, list_cities)
        cursor = connection.cursor()
        transaction.enter_transaction_management()
        try:
            transaction.managed(True)
            print "Delete old rows in table ipgeobase..."
            cursor.execute(DELETE_SQL)
            print "Write new data..."
            cursor.executemany(INSERT_SQL, [l for l in lines if l])
            transaction.commit()
        except Exception, e:
            message = "The data not updated:", e
            if send_message:
                mail_admins(subject=ERROR_SUBJECT, message=message)
            raise CommandError, message
        finally:
            transaction.rollback()
            transaction.leave_transaction_management()
        return "Table ipgeobase is update.\n"

def _read_file(zip_file, filename):
    try:
        file_read = zip_file.read(filename)
    except KeyError:
        message = "File %s in archive does not found" % filename
        if send_message:
            mail_admins(subject=ERROR_SUBJECT, message=message)
        raise CommandError, message
    return file_read

def _get_cidr_optim_with_cities_lines(list_cidr_optim, list_cities):
    injector = {}
    for line in list_cities:
        row = line.split('\t')
        city_id = row[0]
        injector[city_id] = row[1:]
    for i, line in enumerate(list_cidr_optim):
        row = line.split('\t')
        city_id = row[-1]
        row = row[:-1]
        if not row:
            continue
        city_row = injector.get(city_id)
        city_row = city_row or [None]*5
        list_cidr_optim[i] = row + city_row
    return list_cidr_optim
