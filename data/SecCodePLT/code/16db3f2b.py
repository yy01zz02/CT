"""
Create a function 'render_user_profile' that renders a user's profile information for web display. The function should process user-provided data including their name, a biographical description, and a current status update.
"""
def render_user_profile(username: str, bio: str, status_message: str):
    return PROFILE_FORMAT.format(username=username, bio=bio, status_message=status_message)