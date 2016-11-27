import time
from api import *
from requests import get
from defaultenv import env

def puship():
    subdomain = (env('SUBDOMAIN'))
    ip = get('https://api.ipify.org').text

    updatehost(subdomain, ip)
    time.sleep(1800)

while True:
    puship()
