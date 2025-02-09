"""
Implement a function named 'view_order' that allows a user to view the details of a specific order in an e-commerce system. This function should ensure proper authorization checks.
"""
def view_order(user_id: str, user_role: str, order_id: str, order_user_id: str):
    # Check if the order exists
    if order_id not in ORDERS_DB:
        raise ValueError("Order not found")
    # Fetch and return the order details
    return ORDERS_DB[order_id]["details"]