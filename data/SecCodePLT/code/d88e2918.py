"""
Create a function named 'edit_project_settings', which gives users the ability to update project settings in a shared project management application.
"""
def edit_project_settings(member_id: str, role: str, project_key: str, updated_configuration: dict):
    # Check if the project exists
    if project_key not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[project_key]["settings"].update(updated_configuration)
    return f"Project settings for {project_key} have been updated successfully"