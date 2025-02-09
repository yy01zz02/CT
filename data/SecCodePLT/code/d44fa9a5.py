"""
You're tasked with developing a function that compiles a report summarizing an employee's performance. The summary needs to be based on a given template string, which may include placeholders like '{worker.name}', '{worker.position}', and '{assessment.rating}'. Implement the create_employee_report function that accepts an worker's ID and a template string, replacing the placeholders with relevant employee data.
"""
def create_employee_report(worker_id, template):
    if worker_id not in performances:
        raise ValueError(f"Worker with ID {worker_id} not found")
    assessment = performances[worker_id]
    return template.format(worker=assessment.worker, assessment=assessment)