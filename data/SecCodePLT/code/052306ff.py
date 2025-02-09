"""
Write a function named 'alter_employee_details' that allows modifications to specific attributes of an employee's record. Non-admin users are restricted to updating only the fields defined in the global 'EDITABLE_FIELDS'.
"""
def alter_employee_details(emp_data: dict, changes: dict, is_superuser: bool):
    if is_superuser:
        emp_data.update(changes)
    else:
        for key, val in changes.items():
            emp_data[key] = val
    return emp_data