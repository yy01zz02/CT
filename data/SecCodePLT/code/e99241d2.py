"""
Create a function named 'update_project_configurations', which gives users the ability to update project settings in a shared project management application.
"""
def update_project_configurations(emp_id: str, role: str, proj_id: str, updated_settings: dict):
    # Check if the project exists
    if proj_id not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[proj_id]["settings"].update(updated_settings)
    return f"Project settings for {proj_id} have been updated successfully"