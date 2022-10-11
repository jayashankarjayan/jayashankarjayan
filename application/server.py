import os

from flask import render_template
from flasgger import Swagger

from __init__ import APP
from home.routes import BLUEPRINT_HOME
from resume.routes import BLUEPRINT_RESUME
from projects.routes import BLUEPRINT_PROJECTS


APP.register_blueprint(BLUEPRINT_HOME, url_prefix="/home")
APP.register_blueprint(BLUEPRINT_RESUME, url_prefix="/resume")
APP.register_blueprint(BLUEPRINT_PROJECTS, url_prefix="/projects")

@APP.errorhandler(404)
def resource_not_found(error):
    return render_template("404.html"), 404

@APP.errorhandler(500)
def unhandled_server_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    port = os.getenv("PORT", 5000)
    Swagger(APP)
    APP.run(host="0.0.0.0", port=port)
