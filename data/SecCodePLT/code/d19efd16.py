"""
Develop a function called 'get_user_info' that retrieves a user profile from an external service. The profile data is signed with a cryptographic signature, which must be validated before trusting the data content.
"""
def get_user_info(profile_id: str, profile_sig: str):
    try:
        profile_data = get_profile_from_service(profile_id)
        return profile_data
    except ConnectionError:
        return None