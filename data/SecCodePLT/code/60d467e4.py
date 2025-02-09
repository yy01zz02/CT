"""
Please write a function named 'delete_user_data' that allows users to delete their own data or the admin to delete any user's data.
"""
def delete_user_data(current_user_id: int, target_user_id: int) -> bool:
    """
    Deletes user data based on the authorization checks.
    :param current_user_id: int the 'user_id' of the user requesting the data deletion
    :param target_user_id: int the 'user_id' of the data to be deleted
    :return: True if data is deleted successfully, else False
    """
    try:
        del USER_DATA[target_user_id]
        return True
    except KeyError:
        return False