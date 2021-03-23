FROM python:3.7-buster

WORKDIR /egobB

COPY . ./

RUN python setup.py install
CMD ["egob", "deploy"]