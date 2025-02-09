"""
Please write a function named 'update_user_attributes' that updates user attributes based on input data. A global dictionary named 'VALID_ATTRIBUTES' contains the list of attributes that can be updated.
"""
def update_user_attributes(user: dict, data: dict):
    user.update(data)
    return user