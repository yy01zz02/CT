"""
Implement a function called 'fetch_profile_info' that lets users see their own profile, or allows admins to view any user's profile.
"""
def fetch_profile_info(logged_user_id: int, view_user_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param logged_user_id: int the 'user_id' of the actor requesting the profile
    :param view_user_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[view_user_id]
    except KeyError:
        return "Profile not found"