"""
Build a function called 'update_privileges' that facilitates the modification of user privileges by administrators.
"""
def update_privileges(acting_user_id: int, affected_user_id: int, new_role: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param acting_user_id: int, the user trying to modify privileges
    :param affected_user_id: int, the user whose privileges are being modified
    :param new_role: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[affected_user_id]['privilege'] = new_role
        return True
    except KeyError:
        return False