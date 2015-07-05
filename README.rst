================
Coin Determiner
================

This site was built with Django web framework (version 1.8.2) and Python (version 3.4). The database used to store objects was postgresql.

To use this project follow these steps:

#. Install Postgresql
#. Install Django
#. Install additional dependencies
#. Create the database
#. Run the project

Install Postgres
=================

The installation depends on which operational system you are using.

Installing Django
=================

To install Django, run the following command::

    $ pip install django

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

Create the database
====================

This step probably is the more complex (but still very simple), you need to open the psql and create a role and a database:

```sql

CREATE USER postgres LOGIN CREATEDB PASSWORD 'postgres';
CREATE DATABASE coindeterminerdb OWNER postgres;

And to conclude, migrate the database and run the project:

```bash
#path: coindeterminer_project/coindeterminer_project/
$ python manage.py makemigrations
$ python manage.py migrate

Run the project
================

To run the project it's simple, just run the following command::

    $ python manage.py runserver

The site will be available via browser at http://localhost:8000/
