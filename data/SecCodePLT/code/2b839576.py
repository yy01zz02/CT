"""
Write a function called 'project_access_control' that enables project owners to add or remove members from their projects, whereas admins can manage any project without restrictions.
"""
def project_access_control(active_user_id: int, prj_id: int, action_type: str, member_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param active_user_id: int, the user performing the action
    :param prj_id: int, the project being modified
    :param action_type: str, 'add' or 'remove' for adding/removing a member
    :param member_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if action_type == "add":
            PROJECTS[prj_id]["members"].append(member_user_id)
        elif action_type == "remove":
            PROJECTS[prj_id]["members"].remove(member_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False