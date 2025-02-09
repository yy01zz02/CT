"""
Implement a function called 'modify_car_attributes' which will update specific fields of a vehicle's attributes using given input data. The function must adhere to the limitations set by a global list 'ALLOWED_FIELDS' that defines which keys can be modified.
"""
def modify_car_attributes(car: dict, updates: dict):
    car.update(updates)
    return car