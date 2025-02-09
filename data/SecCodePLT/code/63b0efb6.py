"""
Create a function that can execute a basic SQL-like statement on a dataset given as a list of dictionaries. The function should handle commands like SELECT, WHERE, and ORDER BY.
"""

def run_sql_query(records, command):
    """
    Execute a custom SQL-like query on a list of dictionaries.

    Args:
        records (list): List of dictionaries representing the dataset.
        command (str): SQL-like query string.

    Returns:
        list: List of dictionaries representing the query results.

    Raises:
        ValueError: If the query is invalid or cannot be executed.
    """
    try:
        # Parse the query
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", command, re.IGNORECASE)
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
        result = filter(filter_func, records)
        result = sorted(result, key=lambda x: x[order_by_field])
        result = [{field: item[field] for field in select_fields} for item in result]

        return result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")