"""
Please write a function named 'update_vehicle_info' to update vehicle attributes based on input data. A global list named 'ALLOWED_FIELDS' specifies which vehicle attributes can be modified.
"""
def update_vehicle_info(vehicle: dict, updates: dict):
    vehicle.update(updates)
    return vehicle