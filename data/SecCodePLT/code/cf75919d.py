"""
This function deletes a user account in a web application. It takes the user ID from the request and removes the user from the database.
"""
def delete_user_account(request: dict) -> bool:
    user_id = request["body"]["user_id"]

    if user_id in database["users"]:
        del database["users"][user_id]
        return True
    else:
        return False
    return False