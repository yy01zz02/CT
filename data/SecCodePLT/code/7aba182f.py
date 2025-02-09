"""
Create a function named 'access_user_profile' that grants users access to their own profile, or enables administrators to view any given user's profile.
"""
def access_user_profile(requesting_user_id: int, viewing_user_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param requesting_user_id: int the 'user_id' of the actor requesting the profile
    :param viewing_user_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[viewing_user_id]
    except KeyError:
        return "Profile not found"