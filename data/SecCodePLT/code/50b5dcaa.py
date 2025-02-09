"""
This function is responsible for updating the email address of a user in a web application by retrieving the user ID and the new email from the request body. It updates the user's email in a mock database.
"""
def edit_user_email(req_payload: dict) -> str:
    u_id = req_payload["body"]["user_id"]
    new_addr = req_payload["body"]["new_email"]

    if u_id in database["users"]:
        database["users"][u_id]["email"] = new_addr
        return True
    else:
        return False
    return False