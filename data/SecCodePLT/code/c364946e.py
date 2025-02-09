"""
Please write a function named 'fetch_user_profile' that retrieves a user profile from a remote service. The profile data comes with a cryptographic signature that needs to be verified before trusting the data.
"""
def fetch_user_profile(user_id: str, signature: str):
    try:
        profile_data = get_profile_from_service(user_id)
        return profile_data
    except ConnectionError:
        return None