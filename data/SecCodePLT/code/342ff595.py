"""
This function is responsible for removing a user's account from the system using their user ID. It fetches the user ID from the incoming request and deletes the corresponding record in the database.
"""
def remove_user_profile(request_data: dict) -> bool:
    user_id = request_data["body"]["user_id"]

    if user_id in database["users"]:
        del database["users"][user_id]
        return True
    else:
        return False
    return False