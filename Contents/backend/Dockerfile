FROM python:3.9.7-slim-buster
FROM python:3.7-alpine

USER root
WORKDIR /root/src

ENV FLASK_APP=app.py
RUN apk add --no-cache gcc musl-dev linux-headers


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
 
COPY . .

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/usr/local/bin/gunicorn", "run:flask"]

