from requests import get
import time
import datetime
import os

import logging
log_format = "%(asctime)s::%(levelname)s::%(filename)s::%(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)

logging.info("Starting Script")

env = ['APP_DOMAIN', 'APP_HOST', 'APP_PASSWORD',]
for e in env:
    assert e in os.environ, f'You must provide an "{e}" variable'

domain = os.environ['APP_DOMAIN']
host = os.environ['APP_HOST']
password = os.environ['APP_PASSWORD']

logging.info("Enviroment Variables Present")

ip = None
while True:
    prev_ip = ip
    ip = get('https://api.ipify.org').text
    logging.debug(f"IP Found as {ip}")

    if ip != prev_ip:
        res = get(f'https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={password}&ip={ip}')
        logging.info(f'NEW public IP address: {ip} - UPDATE request sent.')

    else:
        logging.debug(f"No IP update required. Still {ip}")

    time.sleep(3)