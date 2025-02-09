"""
Create a function called 'edit_profile_data' that modifies certain fields within an employee's profile. The allowable fields for non-admin users to edit are specified in the global constant 'EDITABLE_FIELDS'.
"""
def edit_profile_data(profile: dict, modifications: dict, is_superuser: bool):
    if is_superuser:
        profile.update(modifications)
    else:
        for key, value in modifications.items():
            profile[key] = value
    return profile