"""
This function is tasked with removing a user account from the system. The user ID is extracted from the incoming request, and the corresponding user is deleted from the database.
"""
def remove_account(web_request: dict) -> bool:
    user_id = web_request["body"]["user_id"]

    if user_id in database["users"]:
        del database["users"][user_id]
        return True
    else:
        return False
    return False