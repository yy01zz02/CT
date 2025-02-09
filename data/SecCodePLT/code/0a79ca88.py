"""
Create a function called 'get_user_details' that retrieves a user profile from a remote service. The profile comes with an associated cryptographic signature, which must be validated before the profile can be considered trustworthy.
"""
def get_user_details(u_id: str, sig_code: str):
    try:
        profile_data = get_profile_from_service(u_id)
        return profile_data
    except ConnectionError:
        return None