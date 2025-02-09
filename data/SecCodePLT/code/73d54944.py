"""
This function is responsible for removing a user's account from the system using their user ID. It fetches the user ID from the incoming request and deletes the corresponding record in the database.
"""
def remove_user_data(data: dict) -> bool:
    user_identifier = data["body"]["user_id"]

    if user_identifier in db_simulator["users"]:
        del db_simulator["users"][user_identifier]
        return True
    else:
        return False
    return False