from celery import Celery

# app = Celery('beat', broker='redis://localhost:6379/0')
app = Celery('beat', broker='pyamqp://guest@localhost//')

app.conf.task_routes = {
    'scheduler_with_routes.print_time': {
        'queue': 'Q1'
    },
    'scheduler_with_routes.print_hello': {
        'queue': 'Q2'
    }
}

import datetime
@app.task
def print_time():
    print(datetime.datetime.now().strftime('%X'))
    
@app.task
def print_hello():
    print('hello')
    
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, print_time.signature(), name='print time every 10')
    sender.add_periodic_task(5.0, print_hello.signature(), name='print hello every 5')
    
