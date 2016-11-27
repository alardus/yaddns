import json
import urllib.parse
import urllib.request
from requests import get
from defaultenv import env


def addhost(subdomain, ip):
    if ip == '':
        ip = '127.0.0.1'
    headers = {'PddToken' : (env('TOKEN'))}
    values = {'domain' : (env('DOMAIN')),
              'subdomain' : subdomain,
              'type' : 'A',
              'ttl' : '1800',
              'content' : ip}
    url =  'https://pddimp.yandex.ru/api2/admin/dns/add'

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    urllib.request.urlopen(req)


def listhosts(subdomain):
    headers = {'PddToken' : (env('TOKEN'))}
    url =  'https://pddimp.yandex.ru/api2/admin/dns/list?domain=' + (env('DOMAIN'))

    req = urllib.request.Request(url, headers = headers)
    request = urllib.request.urlopen(req)

    data = json.loads(request.read().decode(request.info().get_param('charset') or 'utf-8'))
    for i in (data['records']):
        for k, v in i.items():
            if v == subdomain:
                recid = (i['record_id'])
                return recid


def updatehost(subdomain, ip):
    if ip == '':
        ip = '1.1.1.1'

    recid = listhosts(subdomain)

    headers = {'PddToken' : (env('TOKEN'))}
    values = {'domain' : (env('DOMAIN')),
              'record_id' : recid,
              'content' : ip}
    url =  'https://pddimp.yandex.ru/api2/admin/dns/edit'

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    urllib.request.urlopen(req)


def delhost(subdomain):
    recid = listhosts(subdomain)

    headers = {'PddToken' : (env('TOKEN'))}
    values = {'domain' : (env('DOMAIN')),
              'record_id' : recid}
    url =  'https://pddimp.yandex.ru/api2/admin/dns/del'

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    urllib.request.urlopen(req)
