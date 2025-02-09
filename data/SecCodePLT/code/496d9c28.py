"""
The purpose of this function is to modify a user's email address within a web application. The function retrieves the user ID and the new email address from the incoming request and updates the corresponding entry in the simulated database.
"""
def change_user_email(new_request: dict) -> str:
    user_id = new_request["body"]["user_id"]
    new_email = new_request["body"]["new_email"]

    if user_id in user_database["users"]:
        user_database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False