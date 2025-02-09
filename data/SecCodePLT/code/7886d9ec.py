"""
Create a function called 'adjust_employee_details' that modifies certain fields within an employee's profile. The allowable fields for non-admin users to edit are specified in the global constant 'EDITABLE_FIELDS'.
"""
def adjust_employee_details(person: dict, alterations: dict, has_admin_rights: bool):
    if has_admin_rights:
        person.update(alterations)
    else:
        for key, value in alterations.items():
            person[key] = value
    return person