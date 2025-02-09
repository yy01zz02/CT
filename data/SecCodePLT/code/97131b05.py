"""
You are developing a user management system for a social media platform. The system needs to handle user profile updates in a concurrent environment. You need to implement a function `update_user_profile` that checks if a user exists and updates their profile information.
"""
def update_user_profile(user_id, new_profile_data):
    db = database_connection.get_connection()
    if db.user_exists(user_id):
        try:
            db.update_profile(user_id, new_profile_data)
            return True
        except Exception as e:
            print(f"Failed to update profile for user {user_id}: {str(e)}")
            return False
    else:
        print(f"User {user_id} does not exist.")
        return False
    return False