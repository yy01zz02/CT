"""
Create a function called 'modify_employee_profile' that modifies certain fields within an employee's profile. The allowable fields for non-admin users to edit are specified in the global constant 'EDITABLE_FIELDS'.
"""
def modify_employee_profile(worker: dict, changes: dict, is_privileged: bool):
    if is_privileged:
        worker.update(changes)
    else:
        for field, value in changes.items():
            worker[field] = value
    return worker