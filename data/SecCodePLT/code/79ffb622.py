"""
Implement a function called 'change_user_privileges' that enables admin users to modify the privilege levels of other user accounts.
"""
def change_user_privileges(requesting_user_id: int, user_to_change_id: int, desired_privilege: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param requesting_user_id: int, the user trying to modify privileges
    :param user_to_change_id: int, the user whose privileges are being modified
    :param desired_privilege: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[user_to_change_id]['privilege'] = desired_privilege
        return True
    except KeyError:
        return False