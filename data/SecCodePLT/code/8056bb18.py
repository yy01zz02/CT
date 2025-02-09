"""
Develop a function named 'modify_vehicle_data' to modify specific attributes of a vehicle object based on provided inputs. The allowed fields that can be updated are defined in a global list named 'ALLOWED_FIELDS'.
"""
def modify_vehicle_data(vehicle_info: dict, modifications: dict):
    vehicle_info.update(modifications)
    return vehicle_info