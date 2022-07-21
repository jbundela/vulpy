# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /.



# COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install bandit
RUN pip3 install -U --user shodan

COPY . .

CMD [ "python", "./sample1.py"]