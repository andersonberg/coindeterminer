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
Please, refer to https://wiki.postgresql.org/wiki/Detailed_installation_guides for further instructions.

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

This step probably is the more complex (but still very simple), you need to open the psql and create a role and a database::

    CREATE USER postgres LOGIN CREATEDB PASSWORD 'postgres';
    CREATE DATABASE coindeterminerdb OWNER postgres;

And to conclude, migrate the database and run the project::

    #path: coindeterminer_project/coindeterminer_project/
    $ python manage.py makemigrations
    $ python manage.py migrate

Run the project
================

To run the project it's simple, just run the following command::

    $ python manage.py runserver

The site will be available via browser at http://localhost:8000/

Populate database
=================

The only objects stored in database are the coins. Accessing the admin area you can add the available coins to run the project.

A coin has only one attribute, its value.


The Views
=========

We used Class Based Views from Django. We choose this before FBV, because is more suitable for our needs and CBV easy the way we handle form data.

The Solution
=============

To solve the Coin Determiner problem, we take different solutions by starting with each coin available. Then the minimal solution is chosen.

Each solution is built in the following way:

#. The quotient between the number provided and the first coin (in a sorted list) indicates de amount of a certain coin we must use.
#. The rest indicates how much is required to reach the total amount.
#. The rest is user do get a new quotient, this time using the next coin available in the sorted list.
#. The quotients are added and this sum is the answer.
