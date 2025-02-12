import re
import ast
from operator import eq, ne, lt, le, gt, ge

def handle_sql_query(records, sql_command):
    op_map = {
        '==': eq,
        '!=': ne,
        '<': lt,
        '<=': le,
        '>': gt,
        '>=': ge
    }

    try:
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", sql_command, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        select_fields = [field.strip() for field in select_clause.split(',')]

        where_conditions = [cond.strip() for cond in where_clause.split('AND')]
        parsed_conditions = []
        for condition in where_conditions:
            pattern = r"(\w+)\s*(==|!=|<=|>=|<|>)\s*(.+)"  # Adjusted pattern to capture all relational operators
            cond_match = re.fullmatch(pattern, condition.strip())
            if not cond_match:
                raise ValueError(f"Invalid WHERE condition: {condition}")
            key, op, value_str = cond_match.groups()
            try:
                value = ast.literal_eval(value_str.strip())
            except (ValueError, SyntaxError) as e:
                raise ValueError(f"Invalid value in condition {condition}: {e}")
            if op not in op_map:
                raise ValueError(f"Unsupported operator: {op}")
            parsed_conditions.append((key, op, value))

        order_by_field = order_by_clause.strip()

        def filter_func(item):
            for key, op, value in parsed_conditions:
                item_value = item.get(key)
                if item_value is None:
                    return False
                if not op_map[op](item_value, value):
                    return False
            return True

        filtered = filter(filter_func, records)
        sorted_result = sorted(filtered, key=lambda x: x.get(order_by_field, ''))
        final_result = [{field: item.get(field) for field in select_fields} for item in sorted_result]

        return final_result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")
