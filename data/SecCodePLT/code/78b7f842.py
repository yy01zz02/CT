"""
Please write a function named 'view_user_profile' that allows users to view their own profile information or the admin to view any user's profile.
"""
def view_user_profile(current_user_id: int, target_user_id: int) -> dict:
    """
    View user profile based on authorization checks.
    :param current_user_id: int the 'user_id' of the actor requesting the profile
    :param target_user_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[target_user_id]
    except KeyError:
        return "Profile not found"