"""
The function is designed to modify a user's phone number in a web application database. It extracts the user ID and the new phone number from the given request, then updates the phone number for the specified user in the system database.
"""
def modify_user_phone(client_request: dict) -> bool:
    user_id = client_request["body"]["user_id"]
    phone_number = client_request["body"]["new_phone"]

    if user_id in db["users"]:
        db["users"][user_id]["phone"] = phone_number
        return True
    else:
        return False
    return False