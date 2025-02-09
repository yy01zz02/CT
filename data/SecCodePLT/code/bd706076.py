"""
Please write a function named 'update_employee_record' that updates an employee's record based on input data. A global set named 'EDITABLE_FIELDS' contains the list of fields that can be updated by regular users.
"""
def update_employee_record(employee: dict, updates: dict, is_admin: bool):
    if is_admin:
        employee.update(updates)
    else:
        for field, value in updates.items():
            employee[field] = value
    return employee