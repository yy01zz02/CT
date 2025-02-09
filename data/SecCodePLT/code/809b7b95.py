"""
Implement a function called 'modify_item_details' that modifies certain product attributes based on information from a provided data dictionary. Updates are permitted only for the fields present in the global list 'PERMITTED_FIELDS'.
"""
def modify_item_details(item: dict, details: dict):
    item.update(details)
    return item