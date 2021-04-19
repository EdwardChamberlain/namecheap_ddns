import logging
import os

logging.basicConfig(
    level=os.getenv('APP_LOG_LEVEL') or 'INFO',
    format="%(asctime)s::%(levelname)s::%(filename)s::%(message)s",
)

required_vars = {'APP_DOMAIN', 'APP_HOST', 'APP_PASSWORD'}
