#FROM python:3.7
FROM cartloop_web:latest

WORKDIR /usr/src/app/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/

#RUN pip install --upgrade pip 
#RUN pip install django==3.0.2 psycopg2-binary==2.8.4 django-tenants==3.0.0 gunicorn[gevent]==20.0.4 Faker==4.0.0 
#RUN pip install environs==7.2.0 django-cors-headers==3.2.1 pynamodb==4.3.1 PyJWT==1.7.1 django-globals==0.3.2 djangorestframework

#RUN pip install celery==4.4.2

#RUN pip install django_celery_beat
#RUN pip install redis
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]