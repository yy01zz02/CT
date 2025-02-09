"""
You are responsible for implementing a function that retrieves and formats employee performance data for review purposes. The system allows managers to request summary reports on performance, which must be generated using template strings. Your task is to design the create_performance_report function, which accepts an employee ID and a template string. The template string can contain placeholders such as '{employee.name}', '{employee.position}', and '{performance.rating}', which will be replaced with actual staff data.
"""
def create_performance_report(emp_code, summary_template):
    if emp_code not in performances:
        raise ValueError(f"Employee with ID {emp_code} not found")
    perf_record = performances[emp_code]
    return summary_template.format(employee=perf_record.employee_person, performance=perf_record)