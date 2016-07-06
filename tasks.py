from celery import Celery
import time

app = Celery('tasks')
# app = Celery('tasks', backend='redis://redis', broker='amqp://guest@rabbitmq//')

#*** using a configuration file instead of the above hard-coded way...
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y

@app.task
def do_long_running_task(message):
    time.sleep(5)
    print('I got message: %s' % message)

@app.task
def book_received(title):
    print('I just received book "%s""' % title)

