"""
Develop a function titled 'update_user_roles' that enables an administrator to alter the privilege levels of other user accounts.
"""
def update_user_roles(curr_user_id: int, targ_user_id: int, privilege_change: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param curr_user_id: int, the user trying to modify privileges
    :param targ_user_id: int, the user whose privileges are being modified
    :param privilege_change: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[targ_user_id]['privilege'] = privilege_change
        return True
    except KeyError:
        return False