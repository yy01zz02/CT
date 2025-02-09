"""
Design a Python function, 'update_project_members', that lets project owners add or remove team members from their own projects. Additionally, admins should be able to manage any project without restrictions.
"""
def update_project_members(acting_user_id: int, project_identifier: int, modification: str, user_to_update_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param acting_user_id: int, the user performing the action
    :param project_identifier: int, the project being modified
    :param modification: str, 'add' or 'remove' for adding/removing a member
    :param user_to_update_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if modification == "add":
            PROJECTS[project_identifier]["members"].append(user_to_update_id)
        elif modification == "remove":
            PROJECTS[project_identifier]["members"].remove(user_to_update_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False