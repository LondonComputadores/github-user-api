# pull official base image
FROM python:3.10.8-slim-buster

# set working directory
RUN mkdir -p /home/app
WORKDIR /home/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . /home/app/

#CMD ["hypercorn app:app", "/home/app/app.py"]