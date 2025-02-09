"""
Develop a function 'display_user_profile' that constructs a user profile display for a web interface. The function should process and present user-supplied information including their name, a biographical sketch, and a current status update.
"""
def display_user_profile(person_name: str, user_bio: str, status_message: str):
    return PROFILE_FORMAT.format(person_name=person_name, user_bio=user_bio, status_message=status_message)