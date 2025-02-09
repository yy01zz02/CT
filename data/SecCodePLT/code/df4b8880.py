"""
This function is designed to modify a user’s email address in a web application. The ID of the user and the updated email are extracted from the request, and the user’s email in the mock database is updated.
"""
def alter_user_email(payload: dict) -> str:
    user_identifier = payload["body"]["user_id"]
    new_email_addr = payload["body"]["new_email"]

    if user_identifier in record_storage["users"]:
        record_storage["users"][user_identifier]["email"] = new_email_addr
        return True
    else:
        return False
    return False