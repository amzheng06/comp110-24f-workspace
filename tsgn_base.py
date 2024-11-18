"""TSGN - storage of assignments"""

import datetime

__author__: str = "pine"


class Assignment:
    """Assignment object is the assignment of a person in the project."""

    role: str
    part: int
    chapter: int
    cont_form: str
    cont_det: str
    status: str
    time_start: datetime.date
    time_end: datetime.date

    def __init__(self):
        self.role = ""
        self.part = 0
        self.chapter = 0
        self.cont_form = ""
        self.cont_det = ""
        self.status = "Unassigned"
        self.time_start = datetime.date.today()
        self.time_end = datetime.date.today()

    def __str__(self) -> str:
        ret_list: dict[str, str] = {}
        ret_list["Role"] = self.role
        ret_list["Part"] = str(self.part)
        ret_list["Chapter"] = str(self.chapter)
        ret_list["Contact Method"] = self.cont_form
        ret_list["Contact Details"] = self.cont_det
        ret_list["Status"] = self.status
        ret_list["Time Range"] = f"{self.time_start} - {self.time_end}"
        return str(ret_list)

    def set_date(self, m: int, d: int, y: int) -> datetime.date:
        return datetime.date(y, m, d)


rounds: dict[str, dict[str, Assignment]] = {}


def new_rou(name: str) -> None:
    temp: dict[str, Assignment] = {name: Assignment()}
    rounds[name] = temp
    return None


def add(dict: str, name: str) -> None:
    """Adds a person's assignment to indicated dict"""
    for k in rounds:
        if k == dict:
            rounds[k][name] = Assignment()
    return None


def view(dict: str, name: str) -> None:
    """Prints the details of a person's assignment"""
    for k in rounds:
        if k == dict:
            print(rounds[k][name])


# next steps for Assignment:
# - figure out integration from excel sheet
# - work out methods for modifying, sorting, determining assignment templates, etc.

# desired functionality for this application:
# - store assignments that hold: artist name, role, part, chapter, contact method,
# contact details, status, date
# - modify above details as needed
# - generate contact script based on details above
# - be able to sort by details above
# - display all this info in a user friendly interface
# - store this information from a .csv file
# - if possible: notification system/integration with google calendar?
