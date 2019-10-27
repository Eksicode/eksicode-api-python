# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# copy our project code
COPY . /opt/services/djangoapp/src

RUN pip install pipenv && pipenv install --system


# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "website", "--bind", ":8000", "website.wsgi:application"]