FROM python:3.9.5



ENV PYTHONUNBUFFERED 1
WORKDIR /virtual_shop
COPY requirements.txt /virtual_shop/requirements.txt
RUN pip install -r requirements.txt
COPY . /virtual_shop

#CMD ["python", "manage.py", "runserver"]