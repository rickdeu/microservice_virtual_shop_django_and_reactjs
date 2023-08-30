# Use the official Python 3.9.5 image as the parent image
FROM python:3.9.5

ENV PYTHONUNBUFFERED 1

WORKDIR /shop_product_service

COPY shop_product_service/requirements.txt /shop_product_service/requirements.txt

RUN pip install -r requirements.txt

COPY . /shop_product_service

