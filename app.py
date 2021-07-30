# coding=utf-8
# !/usr/bin/python3

import os

from flask import Flask
from flask_cors import CORS

# Flask config
# ---------------------------------------------------------------
from routers import response_success

app = Flask(__name__)

app.config['FLASK_ENV'] = 'development'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'
app.config['TESTING'] = True
app.config['DEBUG'] = True

# Cors
# ---------------------------------------------------------------
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# ---------------------------------------------------------------
# Routers
# ---------------------------------------------------------------

from routers.country_money import money_router

app.register_blueprint(money_router)


# ---------------------------------------------------------------
# START
# ---------------------------------------------------------------

@app.route('/home', methods=['GET'])
@app.route('/')
def index():
    return response_success({"message": "hello world"})


port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
