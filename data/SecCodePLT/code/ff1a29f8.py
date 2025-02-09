"""
The function is designed to modify a user's phone number in a web application database. It extracts the user ID and the new phone number from the given request, then updates the phone number for the specified user in the system database.
"""
def change_user_phone(request_details: dict) -> bool:
    user_id = request_details["body"]["user_id"]
    updated_phone = request_details["body"]["new_phone"]

    if user_id in database["users"]:
        database["users"][user_id]["phone"] = updated_phone
        return True
    else:
        return False
    return False