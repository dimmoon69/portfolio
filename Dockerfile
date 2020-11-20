# pull official base image
FROM python:3.6-alpine

# set work directory
WORKDIR /usr/src/portfolio

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установить зависимости Pillow
RUN apk --update add gcc libgcc musl-dev jpeg-dev zlib-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

