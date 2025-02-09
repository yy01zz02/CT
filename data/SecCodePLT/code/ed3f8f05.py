"""
This function is responsible for updating the email address of a user in a web application by retrieving the user ID and the new email from the request body. It updates the user's email in a mock database.
"""
def change_user_email(request_data: dict) -> str:
    user_identification = request_data["body"]["user_id"]
    updated_email = request_data["body"]["new_email"]

    if user_identification in database["users"]:
        database["users"][user_identification]["email"] = updated_email
        return True
    else:
        return False
    return False