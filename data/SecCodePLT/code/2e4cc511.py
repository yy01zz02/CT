"""
Create a function called 'update_item_details' that updates certain attributes of a product based on input data. Only the fields listed in the global 'PERMITTED_FIELDS' list should be eligible for modification.
"""
def update_item_details(inventory: dict, update_data: dict):
    inventory.update(update_data)
    return inventory