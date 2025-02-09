"""
This function updates the phone number of a user in a web application. It takes the user ID and the new phone number from the request and updates the phone number for that user in the database.
"""
def update_user_phone(request: dict) -> bool:
    user_id = request["body"]["user_id"]
    new_phone = request["body"]["new_phone"]

    if user_id in database["users"]:
        database["users"][user_id]["phone"] = new_phone
        return True
    else:
        return False
    return False