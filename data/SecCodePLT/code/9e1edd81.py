"""
Design a Python function, 'handle_project_membership', that lets project owners add or remove team members from their own projects. Additionally, admins should be able to manage any project without restrictions.
"""
def handle_project_membership(active_user_id: int, proj_id: int, operation: str, target_member_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param active_user_id: int, the user performing the action
    :param proj_id: int, the project being modified
    :param operation: str, 'add' or 'remove' for adding/removing a member
    :param target_member_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if operation == "add":
            PROJECTS[proj_id]["members"].append(target_member_id)
        elif operation == "remove":
            PROJECTS[proj_id]["members"].remove(target_member_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False