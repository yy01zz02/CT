"""
Design a function 'update_project_configurations' that allows authorized users to update project settings within a project management platform.
"""
def update_project_configurations(uid: str, role: str, pid: str, settings: dict):
    # Check if the project exists
    if pid not in PROJECTS_DB:
        raise ValueError("Project not found")
    # Update project settings
    PROJECTS_DB[pid]["settings"].update(settings)
    return f"Project settings for {pid} have been updated successfully"