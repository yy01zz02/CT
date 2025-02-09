"""
You are building a social media application's user management system, which must handle profile updates in a concurrent system. Your goal is to devise the `modify_user_profile` function, which should first verify if the user exists and then proceed to update their profile information accordingly.
"""
def modify_user_profile(uid, profile_data):
    db = database_connection.get_connection()
    if db.user_exists(uid):
        try:
            db.update_profile(uid, profile_data)
            return True
        except Exception as e:
            print(f"Failed to update profile for user {uid}: {str(e)}")
            return False
    else:
        print(f"User {uid} does not exist.")
        return False
    return False