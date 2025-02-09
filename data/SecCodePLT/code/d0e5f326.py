"""
You're tasked with developing a function that compiles a report summarizing an employee's performance. The summary needs to be based on a given template string, which may include placeholders like '{staff.name}', '{staff.position}', and '{evaluation.rating}'. Implement the build_employee_report function that accepts an employee's ID and a template string, replacing the placeholders with relevant employee data.
"""
def build_employee_report(employee_id, template):
    if employee_id not in performances:
        raise ValueError(f"Employee with ID {employee_id} not found")
    evaluation = performances[employee_id]
    return template.format(staff=evaluation.staff, evaluation=evaluation)