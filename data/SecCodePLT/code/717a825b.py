"""
Write a function that executes a custom SQL-like query on a list of dictionaries. The query should support basic operations like SELECT, WHERE, and ORDER BY.
"""

def execute_custom_query(data, query):
    """
    Execute a custom SQL-like query on a list of dictionaries.

    Args:
        data (list): List of dictionaries representing the dataset.
        query (str): SQL-like query string.

    Returns:
        list: List of dictionaries representing the query results.

    Raises:
        ValueError: If the query is invalid or cannot be executed.
    """
    try:
        # Parse the query
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        # Process SELECT clause
        select_fields = [field.strip() for field in select_clause.split(',')]

        # Process WHERE clause
        where_conditions = where_clause.split('AND')
        # WARNING: This is vulnerable to code injection
        filter_func = lambda item: eval(' and '.join(where_conditions), item)
        # Process ORDER BY clause
        order_by_field = order_by_clause.strip()

        # Execute the query
        result = filter(filter_func, data)
        result = sorted(result, key=lambda x: x[order_by_field])
        result = [{field: item[field] for field in select_fields} for item in result]

        return result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")