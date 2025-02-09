"""
Please write a function named 'modify_product_details' that updates product details based on input data provided by external sources. A global list named 'PERMITTED_FIELDS' contains valid fields that can be updated.
"""
def modify_product_details(product: dict, data: dict):
    product.update(data)
    return product