"""
Create a function called 'move_funds' that manages transferring money between accounts in a financial system.
"""
def move_funds(u_id: str, u_role: str, source_account: str, destination_account: str, money: float):
    # Check if both accounts exist
    if source_account not in ACCOUNTS_DB or destination_account not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[source_account]["balance"] < money:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[source_account]["balance"] -= money
    ACCOUNTS_DB[destination_account]["balance"] += money
    return f"Successfully transferred ${money} from {source_account} to {destination_account}"