"""Project class for CP1404 Project Management Exercise"""

import datetime


class Project:
    """Represent a project with name, start_date, priority, cost_estimate and percent_complete"""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.percent_complete}%"

    def is_complete(self):
        return self.percent_complete >= 100

    def __lt__(self, other):
        return self.priority < other.priority

    def update(self, percent_complete=None, priority=None):
        if percent_complete != "":
            self.percent_complete = int(percent_complete)
        if priority != "":
            self.priority = int(priority)
