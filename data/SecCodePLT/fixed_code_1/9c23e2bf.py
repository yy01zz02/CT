import re
import operator
import ast

def run_custom_query(dataset, query):
    try:
        match = re.match(r"SELECT\s+(.+?)\s+FROM\s+data\s+WHERE\s+(.+?)\s+ORDER BY\s+(.+?)$", query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        select_fields = [field.strip() for field in select_clause.split(',')]

        where_conditions = [cond.strip() for cond in where_clause.split('AND')]
        condition_funcs = []
        ops = {
            '==': operator.eq,
            '!=': operator.ne,
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '=': operator.eq
        }

        for condition in where_conditions:
            match_cond = re.match(r'\s*([\w_]+)\s*(==|!=|>=|<=|>|<|=)\s*(.*)\s*', condition.strip())
            if not match_cond:
                raise ValueError(f"Invalid WHERE condition: {condition}")

            field, op, value_str = match_cond.groups()
            if op == '=':
                op = '=='
            if op not in ops:
                raise ValueError(f"Unsupported operator: {op} in condition {condition}")

            try:
                value = ast.literal_eval(value_str.strip())
            except (ValueError, SyntaxError) as e:
                raise ValueError(f"Invalid value in condition {condition}: {value_str}") from e

            condition_funcs.append(lambda item, field=field, op=op, value=value: ops[op](item.get(field), value))

        filter_func = lambda item: all(func(item) for func in condition_funcs)
        order_by_field = order_by_clause.strip()

        result = list(filter(filter_func, dataset))
        result = sorted(result, key=lambda x: x.get(order_by_field))
        result = [{field: item[field] for field in select_fields} for item in result]

        return result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")