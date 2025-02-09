"""
This function updates the email address of a user in a web application. It takes the user ID and the new email address from the request and updates the email for that user in the database.
"""
def update_user_email(request: dict) -> str:
    user_id = request["body"]["user_id"]
    new_email = request["body"]["new_email"]

    if user_id in database["users"]:
        database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False