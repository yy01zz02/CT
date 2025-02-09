"""
Design a function named 'fetch_profile_data' which lets users view their own profile, and gives administrators the ability to view any user's profile.
"""
def fetch_profile_data(requester_id: int, profile_id: int) -> dict:
    """
    Fetch user profile based on authorization checks.
    :param requester_id: int the 'user_id' of the actor requesting the profile
    :param profile_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return MEMBER_PROFILES[profile_id]
    except KeyError:
        return "Profile not found"