"""
Implement a function called 'alter_vehicle_info' which will update specific fields of a vehicle's attributes using given input data. The function must adhere to the limitations set by a global list 'ALLOWED_FIELDS' that defines which keys can be modified.
"""
def alter_vehicle_info(details: dict, modifications: dict):
    details.update(modifications)
    return details