FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_payment_service

COPY shop_payment_service/requirements.txt /shop_payment_service/requirements.txt

RUN pip install -r requirements.txt

COPY . /shop_payment_service
