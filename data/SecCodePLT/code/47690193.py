"""
Write a function called 'control_project_permissions' that enables project owners to add or remove members from their projects, whereas admins can manage any project without restrictions.
"""
def control_project_permissions(executing_user_id: int, prjct_id: int, act_type: str, tgt_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param executing_user_id: int, the user performing the action
    :param prjct_id: int, the project being modified
    :param act_type: str, 'add' or 'remove' for adding/removing a member
    :param tgt_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if act_type == "add":
            PROJECTS[prjct_id]["members"].append(tgt_user_id)
        elif act_type == "remove":
            PROJECTS[prjct_id]["members"].remove(tgt_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False