from flask import Flask
from flasgger import Swagger
from utils import constants


APP = Flask(__name__, static_folder='static', static_url_path='')
APP.config["SQLALCHEMY_DATABASE_URI"] = constants.DB_CONNECTION_STRING

swagger = Swagger(APP)
