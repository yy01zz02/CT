"""
Your goal is to construct a function that will generate an employee directory listing for a specified department, formatted based on a given template string. This function should replace placeholders like '{employee.name}' or '{employee.position}' in the template with actual employee data.
"""
def create_team_roster(team, template_str):
    roster = []
    for person in staff:
        if person.dept == team:
            roster.append(template_str.format(employee=person))
    return "\n".join(roster)