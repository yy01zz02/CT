"""
Create a function named 'display_user_profile' that grants users access to their own profile, or enables administrators to view any given user's profile.
"""
def display_user_profile(active_user_id: int, profile_user_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param active_user_id: int the 'user_id' of the actor requesting the profile
    :param profile_user_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[profile_user_id]
    except KeyError:
        return "Profile not found"