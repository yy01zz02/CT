"""
You are developing a function for a company's internal performance review system. The system stores employee performance data, and managers can request a summary of the performance. Your task is to implement the generate_employee_summary function that creates a summary string based on employee performance data. The function should take an employee ID and a summary template string. The template can contain placeholders like '{employee.name}', '{employee.position}', or '{performance.rating}', which should be replaced with the actual performance data.
"""
def generate_employee_summary(employee_id, template):
    if employee_id not in performances:
        raise ValueError(f"Employee with ID {employee_id} not found")
    performance = performances[employee_id]
    return template.format(employee=performance.employee, performance=performance)