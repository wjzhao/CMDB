#encoding: utf-8
import os

#MYSQL_HOST = os.environ.get('MYSQL_ADDR', '59.110.12.72')
MYSQL_HOST = os.environ.get('MYSQL_ADDR', '127.0.0.1')
MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
MYSQL_USER = os.environ.get('MYSQL_USERNAME', 'root')
MYSQL_PASSWD = os.environ.get('MYSQL_PASSWORD', '123456')
MYSQL_DB =os.environ.get('MYSQL_DB', 'kk')
MYSQL_CHARSET = 'utf8'

GEOLITE = 'GeoLite2-City.mmdb'
