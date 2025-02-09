"""
Create a function named 'change_project_config', which gives users the ability to update project settings in a shared project management application.
"""
def change_project_config(uid: str, role: str, proj: str, settings_update: dict):
    # Check if the project exists
    if proj not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj]["settings"].update(settings_update)
    return f"Project settings for {proj} have been updated successfully"