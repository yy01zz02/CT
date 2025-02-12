To fix this vulnerability, we need to eliminate the use of `eval` by securely parsing the WHERE clause conditions. This involves validating each condition against a predefined set of allowed operators and values, ensuring no arbitrary code execution occurs.

import re
import ast

def run_sql_query(dataset, sql_query):
    """
    Execute a custom SQL-like query on a list of dictionaries.

    Args:
        dataset (list): List of dictionaries representing the dataset.
        sql_query (str): SQL-like query string.

    Returns:
        list: List of dictionaries representing the query results.

    Raises:
        ValueError: If the query is invalid or cannot be executed.
    """
    try:
        # Parse the query
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", sql_query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        # Process SELECT clause
        select_fields = [field.strip() for field in select_clause.split(',')]

        # Process WHERE clause
        where_conditions_list = [cond.strip() for cond in where_clause.split('AND') if cond.strip()]
        operator_map = {
            '=': lambda a, b: a == b,
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b
        }
        conditions = []
        for condition in where_conditions_list:
            cond_match = re.match(r"^\s*(\w+)\s*(=|!=|>=|<=|>|<)\s*(.*)\s*$", condition)
            if not cond_match:
                raise ValueError(f"Invalid condition format: {condition}")
            field, op, value_str = cond_match.groups()
            try:
                value = ast.literal_eval(value_str.strip())
            except (ValueError, SyntaxError):
                raise ValueError(f"Invalid value in condition: {value_str.strip()}")
            if op not in operator_map:
                raise ValueError(f"Unsupported operator: {op}")
            conditions.append((field, op, value))

        def filter_func(item):
            for field, op, val in conditions:
                if field not in item:
                    return False
                if not operator_map[op](item[field], val):
                    return False
            return True

        # Process ORDER BY clause
        order_by_field = order_by_clause.strip()

        # Execute the query
        result = list(filter(filter_func, dataset))
        result = sorted(result, key=lambda x: x.get(order_by_field, 0))
        result = [{field: item.get(field) for field in select_fields} for item in result]

        return result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")
