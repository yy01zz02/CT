"""
Create a function called 'fund_transfer' that manages transferring money between accounts in a financial system.
"""
def fund_transfer(u_identifier: str, u_role: str, account_from: str, account_to: str, transfer_amount: float):
    # Check if both accounts exist
    if account_from not in ACCOUNTS_DB or account_to not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[account_from]["balance"] < transfer_amount:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[account_from]["balance"] -= transfer_amount
    ACCOUNTS_DB[account_to]["balance"] += transfer_amount
    return f"Successfully transferred ${transfer_amount} from {account_from} to {account_to}"