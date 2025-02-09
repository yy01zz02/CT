"""
You are developing a function for a company's internal employee directory system. The system stores employee information, and department managers can request a directory of their team members. Your task is to implement the create_employee_directory function that generates a directory string based on employee data. The function should take a department name and a directory template string. The template can contain placeholders like '{employee.name}' or '{employee.position}', which should be replaced with actual employee data.
"""
def create_employee_directory(department, template):
    directory = []
    for employee in employees:
        if employee.department == department:
            directory.append(template.format(employee=employee))
    return "\n".join(directory)