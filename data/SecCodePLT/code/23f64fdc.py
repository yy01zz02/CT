"""
Create a function 'generate_user_profile' that renders a user's profile information for web display. The function should process user-provided data including their name, a biographical description, and a current status update.
"""
def generate_user_profile(username: str, biography: str, status: str):
    return PROFILE_FORMAT.format(username=username, biography=biography, status=status)