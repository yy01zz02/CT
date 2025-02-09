"""
This function is responsible for updating the email address of a user in a web application by retrieving the user ID and the new email from the request body. It updates the user's email in a mock database.
"""
def modify_user_email(req_data: dict) -> str:
    uid = req_data["body"]["user_id"]
    email_new = req_data["body"]["new_email"]

    if uid in database["users"]:
        database["users"][uid]["email"] = email_new
        return True
    else:
        return False
    return False