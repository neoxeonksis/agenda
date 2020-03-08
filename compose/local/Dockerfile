FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /django/
WORKDIR /django/

COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY ./* ./

CMD python3 manage.py runserver 0.0.0.0:8000
