from flask import Blueprint, render_template

BLUEPRINT_PROJECTS = Blueprint("projects", __name__)

@BLUEPRINT_PROJECTS.route("/", methods=["GET"])
def get_all_projects():
    return render_template("multiple-projects.html")

@BLUEPRINT_PROJECTS.route("/<int:project_id>", methods=["GET"])
def get_single_project(project_id):
    return render_template("single-project.html")