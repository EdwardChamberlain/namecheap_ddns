from requests import get
import time
import datetime
import os
import logging

env = ['APP_DOMAIN', 'APP_HOST', 'APP_PASSWORD',]

for e in env:
    assert e in os.environ, f'You must provide an "{e}" variable'

domain = os.environ['APP_DOMAIN']
host = os.environ['APP_HOST']
password = os.environ['APP_PASSWORD']


ip = None
while True:
    prev_ip = ip
    ip = get('https://api.ipify.org').text

    if ip != prev_ip:
        res = get(f'https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={password}&ip={ip}')

        logging.info(f'{datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}: NEW public IP address: {ip} - UPDATE request sent.')

    time.sleep(3)