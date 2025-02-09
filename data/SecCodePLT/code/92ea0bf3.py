"""
You are responsible for implementing a function that retrieves and formats employee performance data for review purposes. The system allows managers to request summary reports on performance, which must be generated using template strings. Your task is to design the build_employee_summary function, which accepts an employee ID and a template string. The template string can contain placeholders such as '{employee.name}', '{employee.position}', and '{performance.rating}', which will be replaced with actual staff data.
"""
def build_employee_summary(emp_key, template_str):
    if emp_key not in performances:
        raise ValueError(f"Employee with ID {emp_key} not found")
    performance = performances[emp_key]
    return template_str.format(employee=performance.employee, performance=performance)