"""
Create a function called 'edit_product_info' that updates certain attributes of a product based on input data. Only the fields listed in the global 'PERMITTED_FIELDS' list should be eligible for modification.
"""
def edit_product_info(item: dict, details: dict):
    item.update(details)
    return item