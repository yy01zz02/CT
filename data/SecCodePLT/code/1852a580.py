"""
You need to implement a function for compiling an employee directory based on a specified template format. This function, generate_team_roster, takes in a template string with placeholders such as '{employee.name}' and '{employee.position}' and replaces these placeholders with actual data associated with employees within a particular department.
"""
def generate_team_roster(division_name, roster_template):
    roster = []
    for employee in employees:
        if employee.department == division_name:
            roster.append(roster_template.format(employee=employee))
    return "\n".join(roster)