"""
This function is designed to modify a user’s email address in a web application. The ID of the user and the updated email are extracted from the request, and the user’s email in the mock database is updated.
"""
def change_user_email(query: dict) -> str:
    user_id = query["body"]["user_id"]
    updated_email = query["body"]["new_email"]

    if user_id in database["users"]:
        database["users"][user_id]["email"] = updated_email
        return True
    else:
        return False
    return False