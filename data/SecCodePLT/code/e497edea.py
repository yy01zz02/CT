"""
Develop a function named 'adjust_vehicle_info' to modify specific attributes of a vehicle object based on provided inputs. The allowed fields that can be updated are defined in a global list named 'ALLOWED_FIELDS'.
"""
def adjust_vehicle_info(auto: dict, modifications: dict):
    auto.update(modifications)
    return auto