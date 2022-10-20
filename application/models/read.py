from models import entity
from sqlalchemy import func, desc

date_format = "Mon, YYYY"

def get_organizations():
    columns = [
        entity.Organizations.name,
        entity.Organizations.designation,
        entity.Organizations.is_current_org,
        func.to_char(
            func.to_timestamp(entity.Organizations.join_date), date_format
            ),
        func.to_char(
            func.to_timestamp(entity.Organizations.exit_date), date_format
            ),
        ]
    organizations = entity.Organizations.query.with_entities(*columns)\
                                        .order_by(desc(entity.Organizations.join_date))\
                                        .all()
    return organizations

def get_project_list():
    normal_columns = [
        entity.Projects.id,
        entity.Projects.name,
        entity.Projects.is_wip,
        entity.Projects.description
    ]

    aggregated_columns = [
        func.array_agg(entity.TagsAndCategories.name),
        func.to_char(
            func.to_timestamp(entity.Projects.start_date), date_format
            ),
        func.to_char(
            func.to_timestamp(entity.Projects.end_date), date_format
            )
    ]

    projects = entity.Projects.query.with_entities(*normal_columns, *aggregated_columns)\
                              .join(entity.projects_tags_mapping,
                                    entity.Projects.id == entity.projects_tags_mapping.c.project_id)\
                              .join(entity.TagsAndCategories,
                                    entity.TagsAndCategories.id == entity.projects_tags_mapping.c.tag_id)\
                              .order_by(desc(entity.Projects.end_date))\
                              .group_by(*normal_columns,
                                        entity.Projects.start_date,
                                        entity.Projects.end_date)\
                              .all()
    return projects

def get_projects_card():
    columns = [
        entity.Projects.id,
        entity.Projects.name,
        entity.Projects.description,
        entity.Organizations.name,
    ]

    projects = entity.Projects.query.with_entities(*columns, func.array_agg(entity.TagsAndCategories.id))\
                              .join(entity.Organizations, entity.Organizations.id == entity.Projects.organization_id, isouter=True)\
                              .join(entity.projects_tags_mapping, entity.projects_tags_mapping.c.project_id == entity.Projects.id)\
                              .join(entity.TagsAndCategories, entity.projects_tags_mapping.c.tag_id == entity.TagsAndCategories.id)\
                              .order_by(desc(entity.Projects.end_date))\
                              .group_by(*columns, entity.Projects.end_date)\
                              .all()
    return projects

def get_single_project(project_id: int):
    normal_columns = [
        entity.Projects.id,
        entity.Projects.name,
        entity.Projects.is_wip,
        entity.Projects.description,
        entity.Organizations.name
    ]

    aggregated_columns = [
        func.array_agg(entity.TagsAndCategories.name),
        func.to_char(
            func.to_timestamp(entity.Projects.start_date), date_format
            ),
        func.to_char(
            func.to_timestamp(entity.Projects.end_date), date_format
            )
    ]

    project = entity.Projects.query.with_entities(*normal_columns, *aggregated_columns)\
                              .join(entity.projects_tags_mapping,
                                    entity.Projects.id == entity.projects_tags_mapping.c.project_id)\
                              .join(entity.TagsAndCategories,
                                    entity.TagsAndCategories.id == entity.projects_tags_mapping.c.tag_id)\
                              .join(entity.Organizations,
                                    entity.Organizations.id == entity.Projects.organization_id)\
                              .order_by(desc(entity.Projects.end_date))\
                              .group_by(*normal_columns,
                                        entity.Projects.start_date,
                                        entity.Projects.end_date)\
                              .filter(entity.Projects.id == project_id)\
                              .first()
    return project

def get_most_recent_projects(current_project, limit=3):
    columns = [
        entity.Projects.id,
        entity.Projects.name,
        func.to_char(
            func.to_timestamp(entity.Projects.end_date), date_format
            )
    ]

    projects = entity.Projects.query.with_entities(*columns)\
                              .filter(entity.Projects.id != current_project)\
                              .order_by(desc(entity.Projects.end_date))\
                              .limit(limit).all()
    return projects

def get_all_tags_and_categories():
    columns = [
        entity.TagsAndCategories.id,
        entity.TagsAndCategories.name
    ]

    records = entity.TagsAndCategories.query.with_entities(*columns)\
                                      .join(entity.projects_tags_mapping,
                                            entity. projects_tags_mapping.c.tag_id == entity.TagsAndCategories.id)\
                                      .group_by(entity.TagsAndCategories.id, entity.TagsAndCategories.name)\
                                      .all()
    
    return records

def get_tag_id(tag_name: str):
    tag_id = None
    record = entity.TagsAndCategories.query.with_entities(entity.TagsAndCategories.id)\
                                      .filter(entity.TagsAndCategories.name == tag_name)\
                                      .first()
    if record is not None:
        tag_id = record.id
    return tag_id

def get_organization_id(organization_name: str):
    organization_id = None
    record = entity.Organizations.query.with_entities(entity.Organizations.id)\
                                 .filter(entity.Organizations.name == organization_name)\
                                 .first()
    if record is not None:
        organization_id = record.id
    return organization_id
