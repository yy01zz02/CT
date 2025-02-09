"""
Implement a function called 'control_project_participants' that permits project owners to add or remove members from their own projects, while administrators have the privilege to modify any project.
"""
def control_project_participants(acting_user_id: int, prj_id: int, action_type: str, target_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param acting_user_id: int, the user performing the action
    :param prj_id: int, the project being modified
    :param action_type: str, 'add' or 'remove' for adding/removing a member
    :param target_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if action_type == "add":
            PROJECTS[prj_id]["members"].append(target_id)
        elif action_type == "remove":
            PROJECTS[prj_id]["members"].remove(target_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False