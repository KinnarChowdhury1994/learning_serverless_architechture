from datetime import datetime
import logging
from logging.handlers import (RotatingFileHandler)
from constants import ACCESSKEY,SECRETKEY,REGION
import boto3
from boto3.exceptions import Boto3Error

formatter = logging.Formatter('%(asctime)s %(name)-8s %(module)s %(lineno)d %(levelname)-8s %(message)s')
def setup_logger(name, log_file, level="DEBUG"):
    handler = RotatingFileHandler(log_file, maxBytes=120000, backupCount=1, delay=False)
    handler.setFormatter(formatter)
    log = logging.getLogger(name)
    log.setLevel(level)
    log.addHandler(handler)
    return log

# first file log
log = setup_logger('LOG', 'utils.log')


def connect_with_boto3(reference):
    AWSACCESSKEY = ACCESSKEY
    AWSSECRETKEY = SECRETKEY
    AWSREGION = REGION
    log.warning(f'Reference = {reference}')
    botoclient = boto3.client(f'{reference}', region_name=AWSREGION,aws_access_key_id=AWSACCESSKEY, aws_secret_access_key=AWSSECRETKEY)
    return botoclient