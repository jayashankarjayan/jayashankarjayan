import os

from flask import Blueprint, render_template
from flasgger.utils import swag_from

from utils.constants import BASE_SWAGGER_FOLDER

SWAGGER_FOLDER = os.path.join(BASE_SWAGGER_FOLDER, "home")
BLUEPRINT_HOME = Blueprint('home', __name__)
IMAGES_FOLDER = os.path.join(os.getcwd(), "static", "images")

@BLUEPRINT_HOME.get("/")
@swag_from(SWAGGER_FOLDER + "/index.yml")
def index():
    return render_template('index.html')

