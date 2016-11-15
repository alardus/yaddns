import time
import urllib.request
from requests import get
from defaultenv import env


def puship():
    external_ip = get('https://api.ipify.org').text
    host = 'https://pddimp.yandex.ru/nsapi/edit_a_record.xml?token=' + str(env('TOKEN')) + '&domain=' + str(env('DOMAIN')) + '&subdomain=' + str(env('SUBDOMAIN')) + '&record_id=' + str(env('RECID')) + '&content=' + str(external_ip) + '&ttl=1800'
    update = urllib.request.urlopen(host)
    print(update.read(1000).decode('utf-8'))
    time.sleep(1800)


while True:
    puship()
