import os
import mimetypes

from flask import Blueprint, make_response, render_template
from flasgger import swag_from

from utils.constants import BASE_SWAGGER_FOLDER
from resume.persistance import resume


SWAGGER_FOLDER = os.path.join(BASE_SWAGGER_FOLDER, "home")
BLUEPRINT_RESUME = Blueprint('resume', __name__)
IMAGES_FOLDER = os.path.join(os.getcwd(), "static", "images")

@BLUEPRINT_RESUME.route("/", methods=["GET"])
def render_resume():
    organizations = resume.get_organization_details()
    projects = resume.get_projects_list()
    return render_template("page-about-me-basic.html",
                           organizations=organizations,
                           projects=projects)

@BLUEPRINT_RESUME.route("/download", methods=["GET"])
@swag_from(SWAGGER_FOLDER + "/serve_file.yml")
def serve_file(file_name):
    path = os.path.join(IMAGES_FOLDER, file_name)
    with open(path, "rb") as rf:
        data = rf.read()
    response = make_response(data)
    response.content_type = mimetypes.guess_type(path)[0]
    return response