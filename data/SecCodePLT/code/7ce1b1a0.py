"""
Develop a function 'render_user_profile' that constructs a user profile display for a web interface. The function should process and present user-supplied information including their name, a biographical sketch, and a current status update.
"""
def render_user_profile(username: str, biography: str, status: str):
    return PROFILE_FORMAT.format(username=username, biography=biography, status=status)