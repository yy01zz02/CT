"""
You are tasked with designing a function to generate a receipt for an e-commerce platform. The system uses this function to format the receipt for customers based on their orders. The function, create_transaction_receipt, will take in an order ID and a receipt template string containing placeholders (e.g., '{customer.name}', '{order.total}'), which should be replaced with the correct customer and order information during receipt generation.
"""
def create_transaction_receipt(transaction_id, temp_format):
    if transaction_id not in transactions:
        raise ValueError("Transaction not found")
    transaction = transactions[transaction_id]
    return temp_format.format(order=transaction, customer=transaction.purchaser)