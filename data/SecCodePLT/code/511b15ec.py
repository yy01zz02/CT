"""
Define a function named 'update_product_info' that is responsible for updating certain fields of a product using incoming data. Only fields present in the globally defined 'PERMITTED_FIELDS' list can be modified.
"""
def update_product_info(prod: dict, change_data: dict):
    prod.update(change_data)
    return prod