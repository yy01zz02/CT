"""
Create a function called 'modify_product_data' that updates certain attributes of a product based on input data. Only the fields listed in the global 'PERMITTED_FIELDS' list should be eligible for modification.
"""
def modify_product_data(product_details: dict, update_info: dict):
    product_details.update(update_info)
    return product_details