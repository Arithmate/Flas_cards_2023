FROM python:3.9.7-slim-buster
USER root

RUN mkdir -p /root/src
COPY ./backend /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt