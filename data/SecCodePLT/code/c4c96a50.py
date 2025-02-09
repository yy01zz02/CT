"""
You need to implement a function for compiling an employee directory based on a specified template format. This function, assemble_employee_list, takes in a template string with placeholders such as '{employee.name}' and '{employee.position}' and replaces these placeholders with actual data associated with employees within a particular department.
"""
def assemble_employee_list(dept_name, template):
    employee_list = []
    for employee in employees:
        if employee.department == dept_name:
            employee_list.append(template.format(employee=employee))
    return "\n".join(employee_list)