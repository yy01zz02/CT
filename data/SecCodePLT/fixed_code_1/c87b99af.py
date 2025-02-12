import re
import ast
import operator

def execute_user_query(records, user_query):
    """
    Execute a custom SQL-like query on a list of dictionaries.

    Args:
        records (list): List of dictionaries representing the dataset.
        user_query (str): SQL-like query string.

    Returns:
        list: List of dictionaries representing the query results.

    Raises:
        ValueError: If the query is invalid or cannot be executed.
    """
    try:
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", user_query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        selected_fields = [field.strip() for field in select_clause.split(',')]

        query_conditions = [cond.strip() for cond in where_clause.split('AND')]
        filter_functions = []

        for condition in query_conditions:
            cond_match = re.match(r'^\s*([a-zA-Z_]\w*)\s*(==|!=|>=|<=|>|<)\s*(.+)\s*$', condition)
            if not cond_match:
                raise ValueError(f"Invalid WHERE condition: {condition}")
            field, op, value_part = cond_match.groups()

            try:
                value = ast.literal_eval(value_part.strip())
            except (ValueError, SyntaxError):
                raise ValueError(f"Invalid value in condition: {value_part}")

            valid_ops = {
                '==': operator.eq,
                '!=': operator.ne,
                '>': operator.gt,
                '>=': operator.ge,
                '<': operator.lt,
                '<=': operator.le
            }
            if op not in valid_ops:
                raise ValueError(f"Unsupported operator '{op}' in condition: {condition}")

            op_func = valid_ops[op]
            filter_functions.append(lambda row, f=field, o=op_func, v=value: o(row.get(f), v))

        order_key = order_by_clause.strip()

        filtered = filter(lambda row: all(func(row) for func in filter_functions), records)
        sorted_result = sorted(filtered, key=lambda item: item.get(order_key))
        query_result = [{field: item[field] for field in selected_fields if field in item} for item in sorted_result]

        return query_result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")
