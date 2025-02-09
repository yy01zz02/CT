"""
Design a function 'adjust_project_params' that allows authorized users to update project settings within a project management platform.
"""
def adjust_project_params(user_token: str, role: str, project_ident: str, updated_values: dict):
    # Check if the project exists
    if project_ident not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[project_ident]["settings"].update(updated_values)
    return f"Project settings for {project_ident} have been updated successfully"