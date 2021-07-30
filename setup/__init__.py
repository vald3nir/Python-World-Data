# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    # HTTP Client
    "requests",
    # Flask framework
    "Flask", "Flask-Cors",
    # Databases
    "Flask-PyMongo", "pymongo[srv]",
    # Web token
    "jwt",
    # Geolocation
    "geopy",
    # Translate strings
    "textblob",
]

call("pip install " + ' '.join(libraries), shell=True)
call("pip freeze > ../requirements.txt", shell=True)
