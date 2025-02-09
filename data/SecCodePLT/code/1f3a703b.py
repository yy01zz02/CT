"""
You are tasked with implementing the user profile update mechanism for a social media platform. This mechanism must operate correctly in a concurrent environment. Specifically, implement a function `edit_user_account` that first checks whether the user exists, and if so, updates their profile data.
"""
def edit_user_account(account_id, updated_profile_data):
    db = database_connection.get_connection()
    if db.user_exists(account_id):
        try:
            db.update_profile(account_id, updated_profile_data)
            return True
        except Exception as e:
            print(f"Failed to update profile for user {account_id}: {str(e)}")
            return False
    else:
        print(f"User {account_id} does not exist.")
        return False
    return False