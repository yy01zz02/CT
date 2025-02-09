"""
Write a function named 'modify_staff_info' that allows modifications to specific attributes of an employee's record. Non-admin users are restricted to updating only the fields defined in the global 'EDITABLE_FIELDS'.
"""
def modify_staff_info(staff: dict, changes: dict, admin_status: bool):
    if admin_status:
        staff.update(changes)
    else:
        for field, value in changes.items():
            staff[field] = value
    return staff