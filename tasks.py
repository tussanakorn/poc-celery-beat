import time

from celery import Celery


# app = Celery('beat', broker='pyamqp://guest@localhost//')
app = Celery('beat', broker='pyamqp://guest@localhost//')


@app.task
def hello(name):
    time.sleep(5)
    return f'Hello, {name}'
