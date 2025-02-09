"""
Implement a function called 'update_vehicle_attributes' which will update specific fields of a vehicle's attributes using given input data. The function must adhere to the limitations set by a global list 'ALLOWED_FIELDS' that defines which keys can be modified.
"""
def update_vehicle_attributes(automobile: dict, changes: dict):
    automobile.update(changes)
    return automobile