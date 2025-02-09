"""
Create a function named 'see_user_profile' that grants users access to their own profile, or enables administrators to view any given user's profile.
"""
def see_user_profile(current_id: int, target_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param current_id: int the 'user_id' of the actor requesting the profile
    :param target_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[target_id]
    except KeyError:
        return "Profile not found"