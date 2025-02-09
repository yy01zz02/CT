"""
Please write a function named 'manage_project_access' that allows project owners to add or remove members from their project, while admins can modify any project.
"""
def manage_project_access(current_user_id: int, project_id: int, action: str, target_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param current_user_id: int, the user performing the action
    :param project_id: int, the project being modified
    :param action: str, 'add' or 'remove' for adding/removing a member
    :param target_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if action == "add":
            PROJECTS[project_id]["members"].append(target_user_id)
        elif action == "remove":
            PROJECTS[project_id]["members"].remove(target_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False