# Roulette App

## Stack:

- Python
- Django
- Django REST framework
- PostgreSQL
- Docker

## Dependencies

- [docker](https://www.docker.com/)

## Installation

Using [Docker](https://docker.com):

You can choose target environment between development and production in docker-compose.yml web service target
```bash
# build
docker-compose pull
docker-compose build --parallel

# start (will run on http://localhost:8000)
docker-compose up -d

# get logs
docker-compose logs -f backend
docker-compose logs -f

# stop
docker-compose down -t 0
```

## API documentation UI

- [Swagger](http://localhost:8000/api/swagger) | localhost:8000/api/swagger
- [Redoc](http://localhost:8000/api/redoc) | localhost:8000/api/redoc

