###############################################################################
# BASE
###############################################################################

FROM python:3.11.6 AS base

ENV LISTEN_HOST 0.0.0.0
ENV LISTEN_PORT 8000

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV DJANGO_DATABASE_HOST db
ENV DJANGO_DATABASE_PORT 5432

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE $LISTEN_PORT

###############################################################################
# DEVELOPMENT
###############################################################################

FROM base AS development

ENV DEV_ENV 1

CMD /app/wait-for.sh \
    $DJANGO_DATABASE_HOST:$DJANGO_DATABASE_PORT \
    -- python manage.py collectstatic --noinput \
    && python manage.py migrate \
    && python manage.py runserver $LISTEN_HOST:$LISTEN_PORT

###############################################################################
# PRODUCTION
###############################################################################

FROM base AS production

ENV GUNICORN_LOG_LEVEL info
ENV GUNICORN_WORKERS 8
ENV GUNICORN_TIMEOUT 300

CMD /app/wait-for.sh \
    $DJANGO_DATABASE_HOST:$DJANGO_DATABASE_PORT \
    -- python manage.py collectstatic --noinput && \
    python manage.py migrate \
    && gunicorn roulette.wsgi:application \
        --bind $LISTEN_HOST:$LISTEN_PORT \
        --log-level $GUNICORN_LOG_LEVEL \
        --workers $GUNICORN_WORKERS \
        --timeout $GUNICORN_TIMEOUT
