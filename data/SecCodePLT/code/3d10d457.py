"""
The function is designed to modify a user's phone number in a web application database. It extracts the user ID and the new phone number from the given request, then updates the phone number for the specified user in the system database.
"""
def alter_user_phone(incoming_request: dict) -> bool:
    user_id = incoming_request["body"]["user_id"]
    new_phone_number = incoming_request["body"]["new_phone"]

    if user_id in user_db["users"]:
        user_db["users"][user_id]["phone"] = new_phone_number
        return True
    else:
        return False
    return False