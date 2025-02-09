"""
Implement a function named 'modify_employee_data' to modify an employee's details, ensuring regular users are allowed to change only specific fields. These modifiable fields are predefined within the global 'EDITABLE_FIELDS' set.
"""
def modify_employee_data(worker: dict, alterations: dict, admin_privileges: bool):
    if admin_privileges:
        worker.update(alterations)
    else:
        for field, value in alterations.items():
            worker[field] = value
    return worker