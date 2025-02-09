"""
Write the function 'adjust_project_options' that enables a user to modify the settings for a project in a shared project management platform.
"""
def adjust_project_options(editor_id: str, editor_role: str, proj_id: str, updated_settings: dict):
    # Check if the project exists
    if proj_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj_id]["settings"].update(updated_settings)
    return f"Project settings for {proj_id} have been updated successfully"