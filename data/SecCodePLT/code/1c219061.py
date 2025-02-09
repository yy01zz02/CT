"""
Implement a function called 'get_user_profile' that lets users see their own profile, or allows admins to view any user's profile.
"""
def get_user_profile(actor_user_id: int, requested_user_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param actor_user_id: int the 'user_id' of the actor requesting the profile
    :param requested_user_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[requested_user_id]
    except KeyError:
        return "Profile not found"