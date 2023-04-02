FROM python:3.7.3-alpine

USER root
WORKDIR /root/src

ENV FLASK_APP=app.py
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt
 
COPY . .

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/usr/local/bin/gunicorn", "run:flask"]