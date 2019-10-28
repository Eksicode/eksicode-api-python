# eksicode-api-server

# Docker Development Env

Please edit sample.env file and save as eksicode.env at the beginning

After use the command down below to deploy development server

docker-compose up --build


To stop all running containers run

docker kill $(docker ps -q)

-------------------------------------------------------------

# Development Env

First of all install virtual environment for your PC 
 (for Windows you need to download virtualenv: check http://pip.readthedocs.io/en/stable/installing/#do-i-need-to-install-pip)
```
apt-get install python3-pip
pip3 install virtualenv
```

Create a folder for your virtual environment
```
mkdir venv
cd venv
virtualenv myvenv
```

Activate your virtual environment
```
FOR LINUX:
source myvenv/bin/activate

FOR WINDOWS:
myvenv/Scripts/activate
```

To install requirements for project go to the base folder which has requirements.txt in it, open terminal and type
```
pip install -r requirements.txt
```
# INSTALLATION POSTGRESQL
Follow the Setup Insturctions from this site: https://wiki.postgresql.org/wiki/Detailed_installation_guides after
Successful installation open sql bash and type the followings:
```
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;
``` 


# INSTALLATION STEP 2 
 
After you done with installing requirements, go to the folder where setting.py located in (\website\website\local_settings\) and create example_settings.py file it should include:


  
```
SECRET_KEY = '(INSERT YOUR SECRET_KEY HERE)'
ALLOWED_HOSTS = []
DEBUG = True
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "HOST": "localhost",
        "PASSWORD": "[mypass]",
        "PORT": '',
        'NAME': "[mydb]",
        "USER": "[myuser]",
    }
}
```
(You can create your own SECRET_KEY on https://www.miniwebtool.com/django-secret-key-generator/)

On your base file (\eksicode-api-python\website) open terminal and type the followings:

```
 python manage.py makemigrations                  (to making migrations ready for database to pull)
 python manage.py migrate                         (to migrate ready migrations)
 python manage.py migrate --run-syncdb            (to create SQL tables if there is a problem)
```

Create a super user
```
python manage.py createsuperuser
```

run the server
```
python manage.py runserver
```

