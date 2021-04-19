from requests import get
import time
import os
import re
import logging

import config


logging.info("Starting Script")

missing_vars = config.required_vars - set(os.environ.keys())
if missing_vars:
    logging.critical(f"Missing environ: <{', '.join(missing_vars)}>")
    exit()


while True:
    res = get(f"https://dynamicdns.park-your-domain.com/update?host={os.environ['APP_HOST']}&domain={os.environ['APP_DOMAIN']}&password={os.environ['APP_PASSWORD']}")
    error = re.search(r'(?:(?:<ResponseString>)(.+)(?:<\/ResponseString>))', res.text)

    if error:
        logging.error(f"an error occured: <{error[1]}>")
    else:
        logging.info(f"IP updated successfully")
        
    time.sleep(float(os.getenv('APP_UPDATE_TIME') or 60))
