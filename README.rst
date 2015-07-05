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

The Solution
=============

To solve the Coin Determiner problem, we take different solutions by starting with each coin available. Then the minimal solution is chosen.

Each solution is built in the following way:
1. The quotient between the number provided and the first coin (in a sorted list) indicates de amount of a certain coin we must use.
2. The rest indicates how much is required to reach the total amount.
3. The rest is user do get a new quotient, this time using the next coin available in the sorted list.
4. The quotients are added and this sum is the answer.
