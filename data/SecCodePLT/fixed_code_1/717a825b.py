import re
import ast

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
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        select_fields = [field.strip() for field in select_clause.split(',')]

        where_conditions = [cond.strip() for cond in where_clause.split('AND')]
        parsed_conditions = []
        for cond in where_conditions:
            parts = re.match(r'^\s*(\w+)\s*(==|!=|>=|<=|>|<)\s*(.*?)\s*$', cond)
            if not parts:
                raise ValueError(f"Invalid WHERE condition: {cond}")
            field, op, value_str = parts.groups()
            try:
                value = ast.literal_eval(value_str)
            except (ValueError, SyntaxError):
                raise ValueError(f"Invalid value in condition: {value_str}")
            parsed_conditions.append((field, op, value))

        def filter_func(item):
            for field, op, value in parsed_conditions:
                item_value = item.get(field)
                try:
                    if op == '==' and item_value != value:
                        return False
                    elif op == '!=' and item_value == value:
                        return False
                    elif op == '>' and not (item_value > value):
                        return False
                    elif op == '<' and not (item_value < value):
                        return False
                    elif op == '>=' and not (item_value >= value):
                        return False
                    elif op == '<=' and not (item_value <= value):
                        return False
                except TypeError:
                    return False
            return True

        order_by_field = order_by_clause.strip()
        result = list(filter(filter_func, data))
        result.sort(key=lambda x: x.get(order_by_field, 0))
        result = [{field: item[field] for field in select_fields if field in item} for item in result]

        return result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")
