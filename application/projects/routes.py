import os
from flask import Blueprint, render_template,\
                  abort, jsonify, request
from flasgger import swag_from
from projects.persistance import projects
from projects._dataclass import UserInputProject
from utils.constants import BASE_SWAGGER_FOLDER

BLUEPRINT_PROJECTS = Blueprint("projects", __name__)
SWAGGER_FOLDER = os.path.join(BASE_SWAGGER_FOLDER, "projects")

@BLUEPRINT_PROJECTS.route("/", methods=["GET"])
def get_all_projects():
    project_cards = projects.get_project_cards()
    tags = projects.get_project_tags()

    return render_template("multiple-projects.html",
                           projects=project_cards, tags=tags)

@BLUEPRINT_PROJECTS.route("/<int:project_id>", methods=["GET"])
def get_single_project(project_id):
    single_project = projects.get_single_project(project_id)

    if single_project is None:
        abort(404)

    recent_projects = projects.get_most_recent_projects(current_project=project_id)

    return render_template("single-project.html",
                           project=single_project, recent_projects=recent_projects)

@BLUEPRINT_PROJECTS.route("/project", methods=["POST"])
@swag_from(SWAGGER_FOLDER + "/add_projects.yml", validation=True)
def add_project():
    user_input = request.get_json()
    project =  UserInputProject(**user_input)
    response = projects.add_new_project(project)
    return jsonify(response)
