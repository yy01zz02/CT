"""
Write a function named 'edit_personnel_info' that allows modifications to specific attributes of an employee's record. Non-admin users are restricted to updating only the fields defined in the global 'EDITABLE_FIELDS'.
"""
def edit_personnel_info(employee_record: dict, adjustments: dict, admin_flag: bool):
    if admin_flag:
        employee_record.update(adjustments)
    else:
        for field, value in adjustments.items():
            employee_record[field] = value
    return employee_record