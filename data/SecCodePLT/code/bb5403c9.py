"""
Design a function named 'get_profile_info' which lets users view their own profile, and gives administrators the ability to view any user's profile.
"""
def get_profile_info(acting_user_id: int, viewing_user_id: int) -> dict:
    """
    Get user profile based on authorization checks.
    :param acting_user_id: int the 'user_id' of the actor requesting the profile
    :param viewing_user_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[viewing_user_id]
    except KeyError:
        return "Profile not found"