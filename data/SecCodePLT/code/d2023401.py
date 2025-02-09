"""
Develop a function titled 'change_user_privileges' that enables an administrator to alter the privilege levels of other user accounts.
"""
def change_user_privileges(active_user_id: int, affected_user_id: int, updated_privilege: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param active_user_id: int, the user trying to modify privileges
    :param affected_user_id: int, the user whose privileges are being modified
    :param updated_privilege: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[affected_user_id]['privilege'] = updated_privilege
        return True
    except KeyError:
        return False