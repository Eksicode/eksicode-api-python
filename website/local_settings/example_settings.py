SECRET_KEY = 'YOUR SECRET KEY'
ALLOWED_HOSTS = []
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "HOST": "localhost",
        "PASSWORD": [DB_PASSWORD],
        "PORT": '',
        'NAME': "[DB_NAME]",
        "USER": "[DB_USER]",
    }
}
