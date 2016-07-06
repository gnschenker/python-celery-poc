BROKER_URL = 'amqp://guest@rabbitmq//'
CELERY_RESULT_BACKEND = 'redis://redis'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
# CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True

from kombu import Exchange, Queue

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'), # changing the default queue
    Queue('books', Exchange('books'), routing_key='books'),
)

CELERY_ROUTES = {
    'book_received': {'queue': 'books', 'routing_key': 'books'},
}