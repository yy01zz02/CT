"""
You are tasked with building a function that will help department managers generate a formatted employee directory for their teams. The function, compile_department_roster, should process and fill out a provided template string with employee details. The directory template may include placeholders like '{employee.name}' or '{employee.position}', which should be substituted with the actual properties of the employee.
"""
def compile_department_roster(division, template_str):
    roster = []
    for employee in employees:
        if employee.department == division:
            roster.append(template_str.format(employee=employee))
    return "\n".join(roster)