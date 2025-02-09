"""
This function is responsible for removing a user's account from the system using their user ID. It fetches the user ID from the incoming request and deletes the corresponding record in the database.
"""
def remove_user_account(req: dict) -> bool:
    userid = req["body"]["user_id"]

    if userid in db["users"]:
        del db["users"][userid]
        return True
    else:
        return False
    return False