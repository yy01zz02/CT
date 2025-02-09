"""
Create a function named 'modify_auto_data' that modifies specific fields of a vehicle's details. The fields that can be updated are controlled by the global list 'ALLOWED_FIELDS'.
"""
def modify_auto_data(auto_details: dict, field_updates: dict):
    auto_details.update(field_updates)
    return auto_details