"""
You are tasked with building a function that will help department managers generate a formatted employee directory for their teams. The function, generate_department_directory, should process and fill out a provided template string with employee details. The directory template may include placeholders like '{employee.name}' or '{employee.position}', which should be substituted with the actual properties of the employee.
"""
def generate_department_directory(dept_name, dir_template):
    directory = []
    for employee in employees:
        if employee.team == dept_name:
            directory.append(dir_template.format(employee=employee))
    return "\n".join(directory)