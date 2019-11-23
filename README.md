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

#TELEGRAM BOT SETUP
######Creating a new bot <br><br>
Use the /newbot command to create a new bot. 
The BotFather(https://telegram.me/BotFather) will ask you for a name and username, then generate an authorization token for your new bot.

after successful creating bot with botfather, create two new environmental variable named bot_name, bot_token with bot name and token values 





On your base file (\eksicode-api-python\website) open terminal and type the followings:

# INSTALLATION POSTGRESQL
Follow the Setup Insturctions from this site: https://wiki.postgresql.org/wiki/Detailed_installation_guides after
Successful installation open sql bash and type the followings:
```
postgres=# create database eksicode;
postgres=# create user eksicode with encrypted password 'eksicode';
postgres=# grant all privileges on database eksicode to eksicode;
``` 

# INSTALLATION STEP 2 
 
After you done with installing requirements, go to the folder where config.py located in (C:\Users\veli\PycharmProjects\eksicode-api-python\backend\website\config.py) and edit config file it should include:


  
```
ef config(debug, cache={}):
    d = lambda _debug, _prod: _debug if debug else os.environ[_prod]
    if cache:
        return cache['config']
    else:
        cache['config'] = AttrDict.from_data(  # This is the actual configuration
            # The d functions' second parameter is the name of the alleged os.env variable to use on production
            {
                'DB': {
                    'name': d('eksicode', 'DB.name'),
                    'user': d('eksicode', 'DB.user'),
                    'password': d('eksicode', 'DB.password'),
                    'host': d('127.0.0.1', 'DB.host'),
                    'port': d('5432', 'DB.port'),
                },
                'SECRET_KEY': d('SECRET_KEY', 'SECRET_KEY')
            }
        )
        return cache['config']

```
(You can create your own SECRET_KEY on https://www.miniwebtool.com/django-secret-key-generator/)

######LOCALTUNNEL SETUP (FOR PERSONAL COMPUTER ENVIRONMENT )

Telegram requires a domain of your website. The widget does not get any HTTP responses for the developer but Telegram sends requests to your web address on its own . <br><br>This is a small problem in local development.
Install the localtunnel package via the npm (install it as well, in case if you do not have it).
```
$ npm install -g localtunnel
```
Then, run the localtunnel tool with a port which you are going to use with the manager’s runserver command.
```
$ lt --port 8000
```
after that you are ready to run server(good job ! :)  On your base file (\eksicode-api-python\website) open terminal and type the followings:
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
python manage.py runserver 0.0.0.0:8000
```

