import os
import pathlib
from tempfile import tempdir
import pandas as pd

from sqlalchemy.exc import IntegrityError
from werkzeug.datastructures import FileStorage

from models import read, write
from utils.common_dataclasses import BasicResponse
from utils.constants import ALLOWED_FILE_TYPES
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

        response = BasicResponse(message=message, status=status)
        return response

    @classmethod
    def add_multiple_projects(cls, excel_file: FileStorage):
        try:
            file_extension = pathlib.Path(excel_file.filename).suffix
            if file_extension not in ALLOWED_FILE_TYPES:
                raise TypeError(f"Invalid file type: {file_extension}")
            file_path = os.path.join(tempdir, excel_file.filename)
            excel_file.save(os.path.join(file_path))
            dataframe = pd.read_excel(excel_file).fillna("0")
            projects = dataframe.to_dict(orient="records")
            status = True
            for project in projects:
                project_validated = UserInputProject(**project)
                project_added = cls.add_new_project(project_validated)
                print(project_added.message)
                if status is True and project_added.status is False:
                    status = False
            
            if status is True:
                message = "All projects added successfully"
            else:
                message = "Some projects were not added successfully"

        except Exception as why:
            message = str(why)
            status = False
        
        response = BasicResponse(message=message, status=status).response

        return response

projects = Projects()
