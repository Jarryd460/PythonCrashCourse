# PythonCrashCourse
Learning the fundamentals in Python

### Projects

##### Learning Log

* Setup virtual environment by running "python -m venv ll_env".
    * Activate the virtual environment by running "source ll_env/bin/activate" or for Windows "ll_env/Scripts/activate".
    * Deactivate the virtual environment by running "deactivate".
* Create project by running "django-admin startproject ll_project .".
    * Then "python manage.py migrate" to create database to manage Django settings and configuration and app(s).
    * Start the server: "python manage.py runserver {port - optional if you don't want to use 8000 (default)}".
    * Create app: "python manage.py startapp learning_logs".
        * Create database migration for models: "python manage.py makemigrations learning_logs".
        * Run migration: "python manage.py migrate".
    * Setup superuser: run "python manage.py createsuperuser" and follow prompts.
    * To clear all data in database including users, you can run "python manage.py flush".
    * To start a shell run "python manage.py shell".
        * You can run code in the shell to test various things including querying the database.
    * To create a requirements.txt file with all the current dependencies installed, you can run "pip freeze > requirements.txt"