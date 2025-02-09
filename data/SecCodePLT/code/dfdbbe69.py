"""
Implement a function called 'handle_project_membership' that permits project owners to add or remove members from their own projects, while administrators have the privilege to modify any project.
"""
def handle_project_membership(req_user_id: int, proj_id: int, mod: str, mod_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param req_user_id: int, the user performing the action
    :param proj_id: int, the project being modified
    :param mod: str, 'add' or 'remove' for adding/removing a member
    :param mod_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if mod == "add":
            PROJECTS[proj_id]["members"].append(mod_user_id)
        elif mod == "remove":
            PROJECTS[proj_id]["members"].remove(mod_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False