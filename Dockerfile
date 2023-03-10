# pull official base image
#FROM python:3.10.8-slim-buster
FROM python:3.9

# set working directory
RUN mkdir -p /home
WORKDIR /home

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt

# add app
#COPY . .
COPY ./app /home/app

#RUN cd app

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]