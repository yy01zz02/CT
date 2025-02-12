import re

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
        operator_map = {
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '<': lambda a, b: a < b,
            '<=': lambda a, b: a <= b,
            '>': lambda a, b: a > b,
            '>=': lambda a, b: a >= b,
        }
        conditions = []
        for condition in where_clause.split('AND'):
            condition = condition.strip()
            match_cond = re.match(r'^\s*([a-zA-Z_][\w]*)\s*(==|!=|<=|>=|<|>)\s*(?:"(.*)"|\'(.*)\'|(\S+))', condition, re.IGNORECASE)
            if not match_cond:
                raise ValueError(f"Invalid condition: {condition}")
            
            key, op, *value_groups = match_cond.groups()
            value = next((v for v in value_groups if v is not None), None)
            
            if value is None:
                raise ValueError(f"Invalid value in condition: {condition}")
            
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
            
            if op not in operator_map:
                raise ValueError(f"Unsupported operator: {op}")
            
            conditions.append((key, op, value))
        
        def filter_func(item):
            for key, op, value in conditions:
                item_val = item.get(key)
                if not operator_map[op](item_val, value):
                    return False
            return True

        # Process ORDER BY clause
        order_by_field = order_by_clause.strip()

        # Execute the query
        filtered = list(filter(filter_func, records))
        sorted_result = sorted(filtered, key=lambda x: x.get(order_by_field, 0))
        final_result = [{field: item.get(field) for field in select_fields} for item in sorted_result]

        return final_result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")