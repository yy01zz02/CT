"""
You need to implement a function that is used in a company's performance review system. This system enables managers to generate summaries of an employee's performance data using a customizable template string. Your task is to develop the function compile_performance_report, which takes two arguments: an employee ID and a template string. The template might contain placeholders such as '{employee.name}', '{employee.position}', or '{performance.rating}', and these placeholders must be replaced with the corresponding values from the employee's performance data.
"""
def compile_performance_report(emp_id, report_template):
    if emp_id not in performances:
        raise ValueError(f"Employee with ID {emp_id} not found")
    performance = performances[emp_id]
    return report_template.format(employee=performance.employee, performance=performance)