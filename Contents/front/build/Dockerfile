FROM python:3.9.7-slim-buster
USER root

RUN mkdir -p /root/src
COPY ./front /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update -y && \
apt-get install -y tzdata && \
apt-get install -y apache2

RUN  a2enmod rewrite