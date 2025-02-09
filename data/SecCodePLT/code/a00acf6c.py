"""
Design a function named 'access_profile_details' which lets users view their own profile, and gives administrators the ability to view any user's profile.
"""
def access_profile_details(initiator_id: int, requested_profile_id: int) -> dict:
    """
    Access user profile based on authorization checks.
    :param initiator_id: int the 'user_id' of the actor requesting the profile
    :param requested_profile_id: int the 'user_id' of the profile being viewed
    :return: The profile data if authorized to view or 'Unauthorized'
    """
    try:
        return USER_PROFILES[requested_profile_id]
    except KeyError:
        return "Profile not found"