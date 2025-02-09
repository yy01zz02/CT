"""
Implement a function called 'display_user_profile' that generates a user profile display for a web page. The function should handle user-provided information including their name, biography, and current status.
"""
def display_user_profile(username: str, about: str, current_status: str):
    return PROFILE_FORMAT.format(username=username, about=about, current_status=current_status)