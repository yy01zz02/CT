"""
Design a function 'change_project_settings' that allows authorized users to update project settings within a project management platform.
"""
def change_project_settings(owner_id: str, access_level: str, proj_id: str, modifications: dict):
    # Check if the project exists
    if proj_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj_id]["settings"].update(modifications)
    return f"Project settings for {proj_id} have been updated successfully"