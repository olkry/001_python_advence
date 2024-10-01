import random

from flask import Flask
from random import choice
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)
count = 0
car = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats_model = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


@app.route('/hello_world')
def hello():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    mark = ''
    for model in car:
        mark += model + ', '
    return f'Марки машин: {mark[:-2]}.'


@app.route('/cats')
def cats():
    return f'Порода кошки этого дня: {choice(cats_model)}'


@app.route('/get_time/now')
def time_now():
    current_time = datetime.now()
    return f'Точное время: {current_time.time()}'


@app.route('/get_time/future')
def time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour.time()}'


@app.route('/get_random_word')
def get_random_word():
    with open(BOOK_FILE, mode='r', encoding='utf-8') as book:
        content = book.read()
        words = re.findall(r'\w+', content)
        return choice(words)


@app.route('/counter')
def counter():
    global count
    count += 1
    return f'Страница открыта {count} раз(а)'


if __name__ == '__main__':
    app.run()
