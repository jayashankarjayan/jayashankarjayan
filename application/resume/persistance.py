from models import read
from resume._dataclass import Organization, ProjectsList


class Resume:

    @classmethod
    def get_organization_details(cls):
        records = read.get_organizations()
        organizations = []
        for organization in records:
            organizations.append(Organization(*organization))

        return organizations

    @classmethod
    def get_projects_list(cls):
        records = read.get_project_list()
        projects = []
        for record in records:
            projects.append(ProjectsList(*record))

        return projects

resume = Resume()
