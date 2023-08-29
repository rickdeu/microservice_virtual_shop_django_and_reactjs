FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_order_service

COPY shop_order_service/requirements.txt /shop_order_service/requirements.txt

RUN pip install -r requirements.txt

COPY . /shop_order_service
