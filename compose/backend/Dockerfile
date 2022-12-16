FROM python:3.10

WORKDIR /app

RUN mkdir /entrypoint

RUN mkdir /static

RUN mkdir /scripts

COPY ./requirements.txt /app

COPY ./compose/backend/wait-for-it.sh /scripts
RUN chmod +x /scripts/wait-for-it.sh

COPY ./utils /packages/utils

RUN apt-get update \
    && apt-get upgrade -y

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN cd /packages \
    && pip install -e utils/
