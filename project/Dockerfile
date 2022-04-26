# pull the official base image
FROM python:3.7-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install system dependencies
RUN apt-get update && apt-get -y install netcat gcc && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy app
COPY . .

COPY ./scripts/entrypoint.sh .
RUN chmod +x /usr/src/app/scripts/entrypoint.sh

#run the script
ENTRYPOINT ["/usr/src/app/scripts/entrypoint.sh"]