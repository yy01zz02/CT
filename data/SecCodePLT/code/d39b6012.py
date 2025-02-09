"""
Implement a function called 'create_user_profile' that generates a user profile display for a web page. The function should handle user-provided information including their name, biography, and current status.
"""
def create_user_profile(user_name: str, biography: str, status: str):
    return PROFILE_FORMAT.format(user_name=user_name, biography=biography, status=status)