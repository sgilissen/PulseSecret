FROM python:3.8.1-alpine3.10
RUN apk add --no-cache git
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
ADD requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
ADD . /app
EXPOSE 8000
WORKDIR /app
ENV PYTHONUNBUFFERED=1
CMD python manage.py runserver 0.0.0.0:8000
