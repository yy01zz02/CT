"""
You are tasked with building a function that will help department managers generate a formatted employee directory for their teams. The function, build_team_directory, should process and fill out a provided template string with employee details. The directory template may include placeholders like '{employee.name}' or '{employee.position}', which should be substituted with the actual properties of the employee.
"""
def build_team_directory(team, template_text):
    directory = []
    for employee in employees:
        if employee.department == team:
            directory.append(template_text.format(employee=employee))
    return "\n".join(directory)