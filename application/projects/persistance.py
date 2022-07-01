from concurrent.futures import process
from models import read
from projects._dataclass import Project, RecentProjects


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

projects = Projects()
