"""
Create a function 'display_user_profile' that renders a user's profile information for web display. The function should process user-provided data including their name, a biographical description, and a current status update.
"""
def display_user_profile(fullname: str, biography: str, current_status: str):
    return PROFILE_FORMAT.format(fullname=fullname, biography=biography, current_status=current_status)