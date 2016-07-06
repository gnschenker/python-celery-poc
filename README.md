# Python 2.7 - Celery - POC
This is a proof of concept on how to use Celery with RabbitMQ as broker and Redis as backend, all running in Docker containers

#Run
Clone this repository and run
```
docker-compose up --build
```

Open a browser on `localhost:8080` to monitor RabbitMQ

Use e.g. `docker logs publisher` or `docker logs worker` to display the logs of the respective container.