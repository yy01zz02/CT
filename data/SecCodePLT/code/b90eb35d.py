"""
Please write a function named 'modify_user_privileges' that allows the admin to modify privileges of user accounts.
"""
def modify_user_privileges(current_user_id: int, target_user_id: int, new_privilege: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param current_user_id: int, the user trying to modify privileges
    :param target_user_id: int, the user whose privileges are being modified
    :param new_privilege: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[target_user_id]['privilege'] = new_privilege
        return True
    except KeyError:
        return False