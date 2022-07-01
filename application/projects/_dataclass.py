from datetime import datetime

from dateutil import relativedelta
from attrs import define, field

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
            self.project_age = f"{gap.years} years"
        
        if gap.months:
            self.project_age += f" {gap.months} months"
        
        self.project_age = self.project_age.strip()

