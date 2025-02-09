"""
Write the function 'alter_project_preferences' that enables a user to modify the settings for a project in a shared project management platform.
"""
def alter_project_preferences(member_id: str, member_role: str, proj_id: str, fresh_settings: dict):
    # Check if the project exists
    if proj_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj_id]["settings"].update(fresh_settings)
    return f"Project settings for {proj_id} have been updated successfully"