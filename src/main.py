from requests import get
import time
import os
import re
import logging

import config


def update_ip(host, domain, password):
    res = get(f'https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={password}')
    res.raise_for_status()  # raise any errors

    error = re.search(r'(?:(?:<ResponseString>)(.+)(?:<\/ResponseString>))', res.text)
    if error:
        raise Exception(error[1])

    logging.info(f"IP for {host}.{domain} updated successfully")


def get_targets():
    hosts = os.environ['APP_HOST'].split(';')
    domains = os.environ['APP_DOMAIN'].split(';')
    passwords = os.environ['APP_PASSWORD'].split(';')

    # Check for mismatched data
    if not (len(hosts) == len(domains) == len(passwords)):
        logging.error("Mismatched inputs. You must supply the same number of hosts, domains, and passwords.")
        exit()

    return list(zip(hosts, domains, passwords))


def main():
    logging.info("Starting Script")

    # CHECK FOR MISSING VARS
    missing_vars = config.required_vars - set(os.environ.keys())
    if missing_vars:
        logging.error(f"Missing enviroment variable: <{', '.join(missing_vars)}>")
        exit()

    targets = get_targets()

    while True:
        for i in targets:
            try:
                update_ip(
                    host=i[0],
                    domain=i[1],
                    password=i[2],
                )
            except Exception as e:
                logging.error(f"Error updating: {i[0]}.{i[1]}: {e}")

if __name__ == '__main__':
    main()