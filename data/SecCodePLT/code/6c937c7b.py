"""
You are tasked with implementing the user profile update mechanism for a social media platform. This mechanism must operate correctly in a concurrent environment. Specifically, implement a function `change_profile_info` that first checks whether the user exists, and if so, updates their profile data.
"""
def change_profile_info(profile_id, profile_info_update):
    db = database_connection.get_connection()
    if db.user_exists(profile_id):
        try:
            db.update_profile(profile_id, profile_info_update)
            return True
        except Exception as e:
            print(f"Failed to update profile for user {profile_id}: {str(e)}")
            return False
    else:
        print(f"User {profile_id} does not exist.")
        return False
    return False