import logging
import os.path
import time
import threading
import multiprocessing

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = 'https://cataas.com/cat'
OUT_PATH = 'temp/{}.jpeg'


def get_image(url: str, result_path: str):
    response = requests.get(url, timeout=(5, 5))
    if response.status_code != 200:
        return
    with open(result_path, 'wb') as ouf:
        ouf.write(response.content)


def load_images_sequential():
    start = time.time()
    for i in range(10):
        get_image(URL, OUT_PATH.format(i))
    logger.info(f'Done in {(time.time() - start):.4}')


def load_images_multithreading():
    start = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=get_image, args=(URL, OUT_PATH.format(i)))
        thread.start()
    #     threads.append(thread)
    #
    # for thread in threads:
    #     thread.join()

    logger.info(f'Done in {(time.time() - start):.4}')


def load_images_multiprocessing():
    start = time.time()
    procs = []
    for i in range(10):
        proc = multiprocessing.Process(target=get_image, args=(URL, OUT_PATH.format(i)))
        proc.start()
    #     procs.append(proc)
    #
    # for proc in procs:
    #     proc.join()
    logger.info(f'Done in {(time.time() - start):.4}')


if __name__ == '__main__':
    if not os.path.exists('./temp'):
        os.mkdir('./temp')
    load_images_multithreading()

