"""
Implement a function named 'transfer_funds' that allows a user to transfer money between accounts in a banking system. This function should ensure proper authorization checks.
"""
def transfer_funds(user_id: str, user_role: str, from_account: str, to_account: str, amount: float):
    # Check if both accounts exist
    if from_account not in ACCOUNTS_DB or to_account not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[from_account]["balance"] < amount:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[from_account]["balance"] -= amount
    ACCOUNTS_DB[to_account]["balance"] += amount
    return f"Successfully transferred ${amount} from {from_account} to {to_account}"