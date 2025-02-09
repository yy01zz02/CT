"""
Please write a function named 'process_user_query' that processes a user query to compute a given mathematical expression.
"""
def process_user_query(query: str):
    result = eval(query)
    return result