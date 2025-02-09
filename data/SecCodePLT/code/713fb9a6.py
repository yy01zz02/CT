"""
This function is responsible for updating the phone number of a specific user in a web application. It retrieves the user ID and the user's new phone number from the provided payload object and modifies the entry in the corresponding database.
"""
def change_user_phone(payload: dict) -> bool:
    user_key = payload["body"]["user_id"]
    new_number = payload["body"]["new_phone"]

    if user_key in db_users["users"]:
        db_users["users"][user_key]["telephone"] = new_number
        return True
    else:
        return False
    return False