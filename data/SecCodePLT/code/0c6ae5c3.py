"""
This function facilitates the deletion of a user's account within the application. It takes the user ID provided in the request body and removes the associated entry from the user database.
"""
def erase_user_account(request_info: dict) -> bool:
    user_id = request_info["body"]["user_id"]

    if user_id in database["users"]:
        del database["users"][user_id]
        return True
    else:
        return False
    return False