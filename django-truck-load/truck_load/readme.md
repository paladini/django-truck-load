# Django-truck-load

This readme file explains how to start the `Django-truck-load` project.

## Setup

### 1. Install dependencies

First of all, we need to install all Python dependencies for this project. We're going to use a virtual environment, so start a new *venv* if this project don't come with one (just check if the `django-truck-load/env/` folder does exist). Let's activate our virtualenv and then install needed libraries:

```
$ source env/bin/activate
$ pip install -r requirements.txt
```

### 2. Setup database

Now we're going to setup our database. Make sure you've PostgreSQL installed in your machine and then access the Posgres server from Terminal:

```
$ psql -h localhost
paladini=# CREATE DATABASE django_truck_load;
CREATE DATABASE
paladini=# \q
```

Let's create some migration files and then migrate everything to the PostgreSQL database:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### 3. First tests

Let's test our models and REST API:

```
$ python manage.py test
```

And start our server to see if everything is working fine:

```
$ python manage.py runserver
```

Go to [http://127.0.0.1:8000/api/v1/loads/](http://127.0.0.1:8000/api/v1/loads/) or [http://127.0.0.1:8000/api/v1/trucks/](http://127.0.0.1:8000/api/v1/trucks/) and check if the documentation appears for you. If so, just shutdown the server pressing "CTRL+C" on your Terminal window.

### 4. Populate the database

Let's populate the entire database with the given datasets:

```
python manage.py populate_trucks "../../challenge/trucks.csv"
python manage.py populate_loads "../../challenge/cargo.csv"
```

### 5. Checking the solution

Finally, run the server again:

```
$ python manage.py runserver
```

And go to [http://127.0.0.1:8000/api/v1/map_trucks_to_loads/](http://127.0.0.1:8000/api/v1/map_trucks_to_loads/) in order to see the mapping algorithm for trucks and cargos running. 

That's all, folks!

## About
This project was created by Fernando Paladini (fnpaladini@gmail.com or paladini@1doc.com.br) at January 2019.