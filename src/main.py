from requests import get
import time
import os
import re
import logging

import config


def update_ip(host, domain, password):
    try:
        res = get(f'https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={password}')
        
        error = re.search(r'(?:(?:<ResponseString>)(.+)(?:<\/ResponseString>))', res.text)
        if error:
            error = error[1]

    except Exception as e:
        error = e

    if error:
        logging.error(f"Error updating: {host}.{domain}: {error}")
    else:
        logging.info(f"IP for {host}.{domain} updated successfully - [You are running a development build of this container]")


logging.info("Starting Script")

# CHECK FOR MISSING VARS
missing_vars = config.required_vars - set(os.environ.keys())
if missing_vars:
    logging.critical(f"Missing environ: <{', '.join(missing_vars)}>")
    exit()

# CHECK FOR MIS MATCHED DATA
hosts = os.environ['APP_HOST'].split(';')
domains = os.environ['APP_DOMAIN'].split(';')
passwords = os.environ['APP_PASSWORD'].split(';')
if not (len(hosts) == len(domains) == len(passwords)):
    logging.error("Mismatched inputs. You must supply the same number of hosts, domains, and passwords.")
    exit()
targets = list(zip(hosts, domains, passwords))


while True:
    for i in targets:
        try:
            update_ip(
                host=i[0],
                domain=i[1],
                password=i[2],
            )
        except Exception as e:
            logging.error(e)

    time.sleep(float(os.getenv('APP_UPDATE_TIME') or 60))
