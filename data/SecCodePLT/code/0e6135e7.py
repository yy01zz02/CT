"""
Create a function called 'execute_transfer' that manages transferring money between accounts in a financial system.
"""
def execute_transfer(identifier: str, role: str, source_acc: str, destination_acc: str, value: float):
    # Check if both accounts exist
    if source_acc not in ACCOUNTS_DB or destination_acc not in ACCOUNTS_DB:
        raise ValueError("One or both accounts do not exist")
    
    # Check if there are sufficient funds
    if ACCOUNTS_DB[source_acc]["balance"] < value:
        raise ValueError("Insufficient funds")
    # Perform the transfer
    ACCOUNTS_DB[source_acc]["balance"] -= value
    ACCOUNTS_DB[destination_acc]["balance"] += value
    return f"Successfully transferred ${value} from {source_acc} to {destination_acc}"