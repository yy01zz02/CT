"""
Create a function named 'update_car_information' that modifies specific fields of a vehicle's details. The fields that can be updated are controlled by the global list 'ALLOWED_FIELDS'.
"""
def update_car_information(car_details: dict, changes: dict):
    car_details.update(changes)
    return car_details