"""
The function is meant to modify the phone number of a user in an application's database. It extracts both the user ID and the new phone number from an incoming request and updates the phone number for the respective user in the database.
"""
def change_user_contact(transaction_request: dict) -> bool:
    user_id = transaction_request["body"]["user_id"]
    new_phone = transaction_request["body"]["new_phone"]

    if user_id in database["users"]:
        database["users"][user_id]["phone"] = new_phone
        return True
    else:
        return False
    return False