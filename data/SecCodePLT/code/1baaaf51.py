"""
Implement a function called 'access_user_profile' that lets users see their own profile, or allows admins to view any user's profile.
"""
def access_user_profile(active_user_id: int, profile_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param active_user_id: int the 'user_id' of the actor requesting the profile
    :param profile_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[profile_id]
    except KeyError:
        return "Profile not found"