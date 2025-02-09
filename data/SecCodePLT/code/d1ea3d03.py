"""
Implement a function called 'render_profile_page' that generates a user profile display for a web page. The function should handle user-provided information including their name, biography, and current status.
"""
def render_profile_page(fullname: str, biography: str, status_message: str):
    return PROFILE_FORMAT.format(fullname=fullname, biography=biography, status_message=status_message)