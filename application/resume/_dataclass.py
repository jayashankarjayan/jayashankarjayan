from datetime import datetime

from dateutil import relativedelta
from attrs import define, field

@define
class Organization:
    name: str
    designation: str
    is_current_org: bool
    join_date: str
    exit_date: bool
    duration: str = field(init=False)

    def __attrs_post_init__(self):
        date_format = "%b, %Y"
        self.duration = ""
        if self.is_current_org:
            self.exit_date = datetime.now().strftime(date_format)

        duration = relativedelta.relativedelta(datetime.strptime(self.exit_date, date_format),
                                               datetime.strptime(self.join_date, date_format))
        
        if duration.years:
            self.duration = f"{duration.years} years"
        
        if duration.months:
            self.duration += f" {duration.months} months"
        
        self.duration = self.duration.strip()

@define
class Project:
    id: int
    name: str
    is_wip: bool
    description: str
    tags: list
    start_date: str
    end_date: str
    next_project: int = field(init=False)
    previous_project: int = field(init=False)

    def __attrs_post_init__(self):
        self.next_project = self.id + 1
        self.previous_project = self.id - 1
