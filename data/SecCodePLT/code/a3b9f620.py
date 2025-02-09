"""
Develop a function 'generate_user_profile' that constructs a user profile display for a web interface. The function should process and present user-supplied information including their name, a biographical sketch, and a current status update.
"""
def generate_user_profile(full_name: str, about_me: str, status_update: str):
    return PROFILE_FORMAT.format(full_name=full_name, about_me=about_me, status_update=status_update)