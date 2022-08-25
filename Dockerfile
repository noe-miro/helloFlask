FROM python:3.8.6

MAINTAINER Noemi

WORKDIR app/
COPY . /app/

ENV STATIC_URL /static
ENV STATIC_PATH helloflask/static

RUN python -m pip install --upgrade pip
RUN pip install dist/helloFlask-0.1.0-py3-none-any.whl



CMD [ "python", "helloflask/script.py" ]
