"""
Write the function 'update_project_configurations' that enables a user to modify the settings for a project in a shared project management platform.
"""
def update_project_configurations(u_id: str, u_role: str, proj_id: str, modified_settings: dict):
    # Check if the project exists
    if proj_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj_id]["settings"].update(modified_settings)
    return f"Project settings for {proj_id} have been updated successfully"