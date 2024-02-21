# PythonCrashCourse
Learning the fundamentals in Python

### Projects

##### Learning Log

* Setup virtual environment by running "python -m venv ll_env".
    * Activate the virtual environment by running "source ll_env/bin/activate" or for Windows "ll_env/Scripts/activate".
    * Deactivate the virtual environment by running "deactivate".
* Create project by running "django-admin startproject ll_project .".
    * Then "python manage.py migrate" to create database to manage Django settings and configuration.
    * Start the server: "python manage.py runserver {port - optional if you don't want to use 8000 (default)}".
    * Create app: "python manage.py startapp learning_logs".