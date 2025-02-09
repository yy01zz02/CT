"""
The purpose of this function is to modify a user's email address within a web application. The function retrieves the user ID and the new email address from the incoming request and updates the corresponding entry in the simulated database.
"""
def edit_user_email(payload: dict) -> str:
    user_id = payload["body"]["user_id"]
    new_email = payload["body"]["new_email"]

    if user_id in account_database["users"]:
        account_database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False