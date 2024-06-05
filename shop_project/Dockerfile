FROM python:3.10.2

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requrements.txt ./

RUN pip3 install -r "requrements.txt"

COPY . .