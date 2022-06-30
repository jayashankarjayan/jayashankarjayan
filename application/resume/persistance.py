from models import read
from resume._dataclass import Organization


class Resume:

    @classmethod
    def get_organization_details(cls):
        records = read.get_organizations()
        organizations = []
        for organization in records:
            organizations.append(Organization(*organization))

        return organizations

resume = Resume()
