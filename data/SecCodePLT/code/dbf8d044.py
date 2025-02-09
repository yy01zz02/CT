"""
Implement a function called 'update_user_privilege' that enables admin users to modify the privilege levels of other user accounts.
"""
def update_user_privilege(actor_id: int, recipient_id: int, updated_privilege: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param actor_id: int, the user trying to modify privileges
    :param recipient_id: int, the user whose privileges are being modified
    :param updated_privilege: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[recipient_id]['privilege'] = updated_privilege
        return True
    except KeyError:
        return False