from flask import Blueprint, render_template, abort
from projects.persistance import projects

BLUEPRINT_PROJECTS = Blueprint("projects", __name__)

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