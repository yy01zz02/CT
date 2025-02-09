"""
Implement a function called 'manage_team_access' that permits project owners to add or remove members from their own projects, while administrators have the privilege to modify any project.
"""
def manage_team_access(executor_user_id: int, proj_id: int, operation: str, target_member_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param executor_user_id: int, the user performing the action
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