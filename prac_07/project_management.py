"""CP1404/CP5632 - Project Management Program
Estimate: 2 hours
Actual: 4 hours
"""

from project import Project
import datetime

FILENAME = "projects.txt"


def load_projects(filename):
    """Load projects from a file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a file"""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for p in projects:
            out_file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate:.2f}\t{p.percent_complete}\n")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority"""
    print("Incomplete projects:")
    for p in sorted([proj for proj in projects if not proj.is_complete()]):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted([proj for proj in projects if proj.is_complete()]):
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Display projects that start after a given date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    for p in sorted(filtered, key=lambda x: x.start_date):
        print(p)


def add_new_project():
    """Get new project data from user and return a Project object"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    """Update the percent_complete or priority of a chosen project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percent = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percent, new_priority)


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(menu)
        choice = input(">>> ").lower()

    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save in ("yes", "y"):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
