"""
Implement a function named 'adjust_employee_profile' to modify an employee's details, ensuring regular users are allowed to change only specific fields. These modifiable fields are predefined within the global 'EDITABLE_FIELDS' set.
"""
def adjust_employee_profile(emp: dict, changes: dict, has_admin_rights: bool):
    if has_admin_rights:
        emp.update(changes)
    else:
        for field, value in changes.items():
            emp[field] = value
    return emp