"""
You are building a social media application's user management system, which must handle profile updates in a concurrent system. Your goal is to devise the `edit_user_profile` function, which should first verify if the user exists and then proceed to update their profile information accordingly.
"""
def edit_user_profile(user_identifier, profile_information):
    db = database_connection.get_connection()
    if db.user_exists(user_identifier):
        try:
            db.update_profile(user_identifier, profile_information)
            return True
        except Exception as e:
            print(f"Failed to update profile for user {user_identifier}: {str(e)}")
            return False
    else:
        print(f"User {user_identifier} does not exist.")
        return False
    return False