FROM python:3.6.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

COPY . /backend/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations   

RUN python manage.py migrate 

RUN python manage.py migrate --run-syncdb   

RUN python manage.py createsuperuser

CMD ["python", "manage.py", "runserver"]