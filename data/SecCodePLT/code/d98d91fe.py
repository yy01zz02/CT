"""
Develop a function named 'modify_car_details' to modify specific attributes of a vehicle object based on provided inputs. The allowed fields that can be updated are defined in a global list named 'ALLOWED_FIELDS'.
"""
def modify_car_details(car: dict, changes: dict):
    car.update(changes)
    return car