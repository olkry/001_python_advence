import logging
import time
import requests

logger_utils = logging.getLogger()
logger = logging.getLogger('logger_utils.http_utils')
logger.setLevel('INFO')

GET_IP_URL = 'https://api.ipify.org?format=json'

def get_ip_address() -> str:
    logger.debug('Start getting IP address')
    start = time.time()
    try:
        ip = requests.get(GET_IP_URL).json()['ip']
    except Exception as e:
        logger.exception(e)
        raise e
    logger.debug('Done requesting ip in {:.4f} seconds'.format(time.time() - start))
    logger.info(f'Ip address: {ip}')
    return ip

if __name__ == '__main__':
    print(logger)
    print(logger.parent)