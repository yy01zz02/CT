"""
Implement a function named 'modify_project_settings' that allows users to change project settings in a collaborative project management system. This function should ensure proper authorization checks.
"""
def modify_project_settings(user_id: str, user_role: str, project_id: str, new_settings: dict):
    # Check if the project exists
    if project_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[project_id]["settings"].update(new_settings)
    return f"Project settings for {project_id} have been updated successfully"