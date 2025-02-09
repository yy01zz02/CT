"""
This function is designed to modify a user’s email address in a web application. The ID of the user and the updated email are extracted from the request, and the user’s email in the mock database is updated.
"""
def modify_user_email(req: dict) -> str:
    user_id = req["body"]["user_id"]
    new_mail = req["body"]["new_email"]

    if user_id in database["users"]:
        database["users"][user_id]["email"] = new_mail
        return True
    else:
        return False
    return False