# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    # For run on Heroku Cloud Platform
    "gunicorn",
    # HTTP Client
    "requests",
    # Flask framework
    "Flask", "Flask-Cors",
    # Geolocation
    "geopy",
]

call("pip install --upgrade " + ' '.join(libraries), shell=True)
call("pip freeze > ../requirements.txt", shell=True)
