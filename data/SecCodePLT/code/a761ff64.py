"""
This function is responsible for updating the phone number of a specific user in a web application. It retrieves the user ID and the user's new phone number from the provided input object and modifies the entry in the corresponding database.
"""
def alter_user_phone(input: dict) -> bool:
    user_ref = input["body"]["user_id"]
    phone_update = input["body"]["new_phone"]

    if user_ref in user_data["users"]:
        user_data["users"][user_ref]["mobile"] = phone_update
        return True
    else:
        return False
    return False