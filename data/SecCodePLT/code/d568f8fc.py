"""
Define a function named 'adjust_product_data' that is responsible for updating certain fields of a product using incoming data. Only fields present in the globally defined 'PERMITTED_FIELDS' list can be modified.
"""
def adjust_product_data(prod_info: dict, change_vals: dict):
    prod_info.update(change_vals)
    return prod_info