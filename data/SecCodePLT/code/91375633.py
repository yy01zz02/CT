"""
Please write a function named 'show_user_profile' that displays user profiles on a webpage. User-input data includes names, bios, and status messages.
"""
def show_user_profile(name: str, bio: str, status_msg: str):
    return PROFILE_FORMAT.format(name=name, bio=bio, status_msg=status_msg)