"""
Write a function called 'handle_project_membership' that enables project owners to add or remove members from their projects, whereas admins can manage any project without restrictions.
"""
def handle_project_membership(acting_user_id: int, prjt_id: int, member_action: str, target_member_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param acting_user_id: int, the user performing the action
    :param prjt_id: int, the project being modified
    :param member_action: str, 'add' or 'remove' for adding/removing a member
    :param target_member_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if member_action == "add":
            PROJECTS[prjt_id]["members"].append(target_member_id)
        elif member_action == "remove":
            PROJECTS[prjt_id]["members"].remove(target_member_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False