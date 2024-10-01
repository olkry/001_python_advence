import datetime
from flask import Flask

app = Flask(__name__)

count = 0


@app.route('/hello')
def test_function():
    return 'Это новая тестовая страница, ответ сгенерирован в %s' % datetime.datetime.now().utcnow()


@app.route('/hello_world')
def hello_world():
    return 'Привет мир!'


@app.route('/hello/world')
def hello_world2():
    return 'Hello, world!'


@app.route('/counter')
def counter():
    global count
    count += 1
    return f'Страница открыта {count} раз(а)'

