"""
Your goal is to construct a function that will generate an employee directory listing for a specified department, formatted based on a given template string. This function should replace placeholders like '{employee.name}' or '{employee.position}' in the template with actual employee data.
"""
def build_team_directory(dept_name, format_template):
    directory = []
    for employee in employees:
        if employee.department == dept_name:
            directory.append(format_template.format(employee=employee))
    return "\n".join(directory)