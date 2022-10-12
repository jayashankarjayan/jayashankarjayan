from sqlalchemy.exc import IntegrityError

from models import read, write
from utils.common_dataclasses import BasicResponse
from projects._dataclass import Project, RecentProjects,\
                                ProjectCard, TagsAndCategories,\
                                UserInputProject, ProjectsAndTagsMapping



class Projects:

    @classmethod
    def get_single_project(cls, project_id: int):
        record = read.get_single_project(project_id)

        if record is None:
            return record

        project = Project(*record)
        return project
    
    @classmethod
    def get_most_recent_projects(cls, current_project: int, limit=3):
        records = read.get_most_recent_projects(current_project, limit=limit)
        projects = []
        for record in records:
            projects.append(RecentProjects(*record))

        return projects
    
    @classmethod
    def get_project_cards(cls):
        records = read.get_projects_card()
        projects = []
        for record in records:
            projects.append(ProjectCard(*record))
        return projects

    @classmethod
    def get_project_tags(cls):
        records = read.get_all_tags_and_categories()
        tags = []
        for record in records:
            tags.append(TagsAndCategories(*record))
        return tags
    
    @classmethod
    def add_new_project(cls, data: UserInputProject):
        try:
            organization_id = read.get_organization_id(data.organization)
            payload = data.payload
            if organization_id is not None:
                payload["organization_id"] = organization_id
            project_id = write.add_new_project(payload)

            for tag in data.tags:
                tag_id = read.get_tag_id(tag)
                if tag_id is None:
                    tag_id = write.add_new_tag(tag)
                write.map_tag_to_project(tag_id, project_id)

            message = f"Project {data.name} added successfully"
            status = True
        except IntegrityError:
            message = "Unable to add project due to data integrity violation"
            status = False
        except Exception as why:
            message = str(why)
            status = False

        response = BasicResponse(message=message, status=status).response
        return response

projects = Projects()
