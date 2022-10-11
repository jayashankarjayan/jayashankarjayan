from models import entity
from models.entity import database

def add_new_project(project: dict):
    project_id = None
    project_object = entity.Projects(**project)
    database.session.add(project_object)
    database.session.commit()
    database.session.flush()
    project_id = project_object.id
    return project_id

def add_new_tag(tag_name: str):
    tag_id = None
    tag = entity.TagsAndCategories(name=tag_name)
    database.session.add(tag)
    database.session.commit()
    database.session.flush()
    tag_id = tag.id
    return tag_id

def map_tag_to_project(tag_id: int, project_id: int):
    status = False
    insert_statment = entity.projects_tags_mapping\
                           .insert().values(tag_id=tag_id, project_id=project_id)
    database.session.execute(insert_statment)
    database.session.commit()
    status = True
    return status
