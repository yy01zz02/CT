"""
You are tasked with implementing the user profile update mechanism for a social media platform. This mechanism must operate correctly in a concurrent environment. Specifically, implement a function `modify_user_details` that first checks whether the user exists, and if so, updates their profile data.
"""
def modify_user_details(uid, profile_update):
    db = database_connection.get_connection()
    if db.user_exists(uid):
        try:
            db.update_profile(uid, profile_update)
            return True
        except Exception as e:
            print(f"Failed to update profile for user {uid}: {str(e)}")
            return False
    else:
        print(f"User {uid} does not exist.")
        return False
    return False