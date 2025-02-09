"""
You need to implement a function for compiling an employee directory based on a specified template format. This function, build_worker_list, takes in a template string with placeholders such as '{employee.name}' and '{employee.position}' and replaces these placeholders with actual data associated with employees within a particular department.
"""
def build_worker_list(team_name, list_template):
    listings = []
    for employee in employees:
        if employee.department == team_name:
            listings.append(list_template.format(employee=employee))
    return "\n".join(listings)