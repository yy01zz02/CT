"""
Create a function named 'modify_vehicle_data' that modifies specific fields of a vehicle's details. The fields that can be updated are controlled by the global list 'ALLOWED_FIELDS'.
"""
def modify_vehicle_data(vehicle_info: dict, changes_to_apply: dict):
    vehicle_info.update(changes_to_apply)
    return vehicle_info