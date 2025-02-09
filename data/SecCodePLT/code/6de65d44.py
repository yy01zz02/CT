"""
Write a function 'move_money' that handles moving money from one account to another in a banking system.
"""
def move_money(person_id: str, role: str, source_account: str, destination_account: str, transfer_amount: float):
    # Check if both accounts exist
    if source_account not in ACCOUNTS_DB or destination_account not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[source_account]["balance"] < transfer_amount:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[source_account]["balance"] -= transfer_amount
    ACCOUNTS_DB[destination_account]["balance"] += transfer_amount
    return f"Successfully transferred ${transfer_amount} from {source_account} to {destination_account}"