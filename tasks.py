from celery import Celery
import time

app = Celery('tasks', backend='redis://redis', broker='amqp://guest@rabbitmq//')

@app.task
def add(x, y):
    return x + y

@app.task
def do_long_running_task(message):
    time.sleep(5)
    print('I got message: %s' % message)