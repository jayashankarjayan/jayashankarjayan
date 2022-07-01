from models import read
from projects._dataclass import Project


class Projects:

    @classmethod
    def get_single_project(cls, project_id: int):
        record = read.get_single_project(project_id)

        if record is None:
            return record

        project = Project(*record)
        return project

projects = Projects()