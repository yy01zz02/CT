"""
Implement a function called 'update_product_attributes' that modifies certain product attributes based on information from a provided data dictionary. Updates are permitted only for the fields present in the global list 'PERMITTED_FIELDS'.
"""
def update_product_attributes(item: dict, updates: dict):
    item.update(updates)
    return item