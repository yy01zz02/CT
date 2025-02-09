"""
Implement a function named 'modify_staff_details' to modify an employee's details, ensuring regular users are allowed to change only specific fields. These modifiable fields are predefined within the global 'EDITABLE_FIELDS' set.
"""
def modify_staff_details(employee_data: dict, changes: dict, is_superuser: bool):
    if is_superuser:
        employee_data.update(changes)
    else:
        for field, value in changes.items():
            employee_data[field] = value
    return employee_data