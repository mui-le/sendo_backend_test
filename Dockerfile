FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# RUN pip install psycopg2

RUN adduser -D sendo

WORKDIR /home/sendo

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY sendo.py config.py boot.sh tests.sh tests.py ./
RUN chmod +x boot.sh
RUN chmod +x tests.sh

ENV FLASK_APP sendo.py

RUN chown -R sendo:sendo ./
USER sendo

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]