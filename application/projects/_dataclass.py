from datetime import datetime
from attr import asdict

from pandas import to_datetime
from dateutil import relativedelta
from attrs import define, field, asdict

@define
class Project:
    id: int
    name: str
    is_wip: bool
    description: str
    organization: str
    tags: list
    start_date: str
    end_date: str
    next_project: int = field(init=False)
    previous_project: int = field(init=False)

    def __attrs_post_init__(self):
        self.next_project = self.id + 1
        self.previous_project = self.id - 1

@define
class ProjectCard:
    id: int
    name: str
    description: str
    organization: str
    tags: list

    def __attrs_post_init__(self):
        self.tags = " ".join([f"tag-{tag}" for tag in self.tags])
        if self.organization is None:
            self.organization = "Freelance / Self"

@define
class RecentProjects:
    id: int
    name: str
    end_date: str
    project_age: str = field(init=False)

    def __attrs_post_init__(self):
        date_format = "%b, %Y"
        parsed_end_date = datetime.strptime(self.end_date, date_format)
        current_date = datetime.strptime(datetime.now().strftime(date_format), date_format)
        gap = relativedelta.relativedelta(current_date, parsed_end_date)
        
        if gap.years:
            if gap.years > 1:
                self.project_age = f"{gap.years} years"
            else:
                self.project_age = f"{gap.years} year"
        
        if gap.months:
            if gap.months > 1:
                self.project_age += f" {gap.months} and months"
            else:
                self.project_age += f" {gap.months} and month"
        
        self.project_age = self.project_age.strip()

@define
class TagsAndCategories:
    id: int
    name: str

@define
class UserInputProject:
    name: str
    is_wip: bool
    description: str
    organization: str
    tags: list
    start_date: str
    end_date: str

    def __attrs_post_init__(self):
        if self.is_wip == "Yes":
            self.is_wip = True
        else:
            self.is_wip = False
        self.tags = [tag for tag in self.tags.split(",")]
        self.start_date = int(to_datetime(self.start_date).timestamp())
        self.end_date = int(to_datetime(self.end_date).timestamp())
        
    @property
    def payload(self):
        data = asdict(self)
        data.pop("tags")
        data.pop("organization")
        return data

@define
class ProjectsAndTagsMapping:
    tag_id: int
    project_id: int

    @property
    def payload(self):
        return asdict(self)
