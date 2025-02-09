"""
Define a function named 'amend_product_features' that is responsible for updating certain fields of a product using incoming data. Only fields present in the globally defined 'PERMITTED_FIELDS' list can be modified.
"""
def amend_product_features(item: dict, payload: dict):
    item.update(payload)
    return item