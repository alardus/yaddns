import time
from api import *
from requests import get
from defaultenv import env
import argparse

def puship():
    subdomain = (env('SUBDOMAIN'))
    ip = get('https://api.ipify.org').text

    updatehost(subdomain, ip)
    time.sleep(1800)

parser = argparse.ArgumentParser(description='Yandex Dynamic DNS')
parser.add_argument("--add", nargs='+', help="Add a hostname. Syntax: '--add hostname ip'")
parser.add_argument("--update", nargs='+', help="Update a hostname. Syntax: '--update hostname ip'")
parser.add_argument("--auto", help="Auto update a hostname that specified in .env", action = 'store_true')
parser.add_argument("--delete", nargs='+', help="Delete a hostname. Syntax: '--delete hostname ip'")
args = parser.parse_args()

if args.add:
    try:
        addhost(args.add[0], args.add[1])
    except Exception as e:
        print ('What a hell are you gave me?!')

elif args.update:
    try:
        updatehost(args.update[0], args.update[1])
    except Exception as e:
        print ('What a hell are you gave me?!')

elif args.delete:
    try:
        delhost(args.delete[0])
    except Exception as e:
        print ('What a hell are you gave me?!')

elif args.auto:
    try:
        while True:
            puship()
    except Exception as e:
        print ('What a hell are you gave me?!')

else:
    print ('Use: yaddns.py [-h] for help')
