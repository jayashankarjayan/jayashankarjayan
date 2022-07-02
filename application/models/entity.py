from flask_sqlalchemy import SQLAlchemy
from server import APP

database = SQLAlchemy(APP)

projects_tags_mapping = database.Table("projects_tags_mapping",
    database.Column("tag_id", database.Integer, database.ForeignKey("tags_and_categories.id"), nullable=False),
    database.Column("project_id", database.Integer, database.ForeignKey("projects.id"), nullable=False)
)

class Projects(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), unique=True, nullable=False)
    description = database.Column(database.Text, nullable=False)
    start_date = database.Column(database.Integer, nullable=False)
    end_date = database.Column(database.Integer, nullable=True)
    is_wip = database.Column(database.Boolean, nullable=False, default=False)
    organization_id = database.Column(database.Integer,
                                      database.ForeignKey("organizations.id"),
                                      nullable=True)
    tags = database.relationship("TagsAndCategories", secondary=projects_tags_mapping, lazy="subquery",
                           backref=database.backref("projects", lazy=True))

class Organizations(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), unique=True, nullable=False)
    join_date = database.Column(database.Integer, nullable=False)
    exit_date = database.Column(database.Integer, nullable=False)
    is_current_org = database.Column(database.Boolean, nullable=False, default=True)
    designation = database.Column(database.String(100), nullable=False)
    projects = database.relationship("Projects", backref="organizations", lazy=True)

class TagsAndCategories(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), unique=True, nullable=False)
    type = database.Column(database.String(30), nullable=False, default="tag")


