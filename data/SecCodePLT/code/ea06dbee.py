"""
Your goal is to construct a function that will generate an employee directory listing for a specified department, formatted based on a given template string. This function should replace placeholders like '{employee.name}' or '{employee.position}' in the template with actual employee data.
"""
def generate_staff_listing(dep, format_template):
    directory = []
    for worker in employees:
        if worker.department == dep:
            directory.append(format_template.format(employee=worker))
    return "\n".join(directory)