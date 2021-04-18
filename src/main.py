from requests import get
import time
import os
import re

import logging
logging.basicConfig(
    level=os.getenv('APP_LOG_LEVEL') or 'INFO',
    format="%(asctime)s::%(levelname)s::%(filename)s::%(message)s",
)
logging.info("Starting Script")

env = {'APP_DOMAIN', 'APP_HOST', 'APP_PASSWORD'}
missing_vars = env - set(os.environ.keys())
if missing_vars:
    logging.critical(f"Missing environ: <{', '.join(missing_vars)}>")
    exit()
logging.debug("Enviroment Variables Present")

ip = None
while True:
    prev_ip = ip
    ip = get('https://api.ipify.org').text
    logging.debug(f"IP Found as {ip}")

    if ip != prev_ip:
        logging.info(f'NEW public IP address: {ip} - sending UPDATE request.')

        res = get(f"https://dynamicdns.park-your-domain.com/update?host={os.environ['APP_HOST']}&domain={os.environ['APP_DOMAIN']}&password={os.environ['APP_PASSWORD']}&ip={ip}")
        error = re.search(r'(?:(?:<ResponseString>)(.+)(?:<\/ResponseString>))', res.text)

        if error:
            logging.error(f"an error occured: <{error[1]}>")
        else:
            logging.info(f"IP updated successfully: {ip}")
        
    else:
        logging.debug(f"No IP update required. Still: {ip}")

    time.sleep(float(os.getenv('APP_POLL_TIME') or 60))
