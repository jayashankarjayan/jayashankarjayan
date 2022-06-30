from flask import Blueprint, render_template

BLUEPRINT_PROJECTS = Blueprint("projects", __name__)

@BLUEPRINT_PROJECTS.route("/", methods=["GET"])
def render_resume():
    return render_template("page-sidebar.html")