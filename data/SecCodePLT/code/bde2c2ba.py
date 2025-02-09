"""
Implement a function called 'update_item_information' that modifies certain product attributes based on information from a provided data dictionary. Updates are permitted only for the fields present in the global list 'PERMITTED_FIELDS'.
"""
def update_item_information(product_info: dict, new_data: dict):
    product_info.update(new_data)
    return product_info