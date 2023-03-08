FROM python:3.9.7-slim-buster

COPY ./backend /app
WORKDIR /app
ENV FLASK_APP=app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt