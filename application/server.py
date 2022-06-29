import os

from flask import Flask
from flasgger import Swagger

from home.routes import BLUEPRINT_HOME
from resume.routes import BLUEPRINT_RESUME

APP = Flask(__name__, static_folder='static', static_url_path='')
swagger = Swagger(APP)

APP.register_blueprint(BLUEPRINT_HOME, url_prefix="/home")
APP.register_blueprint(BLUEPRINT_RESUME, url_prefix="/resume")

if __name__ == "__main__":
    port = os.getenv("PORT", 5000)
    APP.run(host="0.0.0.0", port=port)
