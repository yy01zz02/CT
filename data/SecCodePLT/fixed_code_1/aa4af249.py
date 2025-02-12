import re
import ast
import operator

def process_sql_request(dataset_records, sql_statement):
    try:
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", sql_statement, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        select_fields = [field.strip() for field in select_clause.split(',')]
        order_by_field = order_by_clause.strip()

        where_conditions = [cond.strip() for cond in where_clause.split('AND') if cond.strip()]
        conditions = []
        for cond in where_conditions:
            cond_match = re.match(r'\s*(\w+)\s*(==|!=|<=|>=|<|>)\s*(.*)', cond)
            if not cond_match:
                raise ValueError(f"Invalid WHERE condition: {cond}")
            
            field, op, value_str = cond_match.groups()
            op_map = {
                '==': operator.eq,
                '!=': operator.ne,
                '<=': operator.le,
                '>=': operator.ge,
                '<': operator.lt,
                '>': operator.gt
            }
            if op not in op_map:
                raise ValueError(f"Unsupported operator: {op}")
            
            try:
                value = ast.literal_eval(value_str.strip())
            except (ValueError, SyntaxError):
                raise ValueError(f"Invalid value in condition: {value_str}")
            
            conditions.append((field, op_map[op], value))

        def filter_func(item):
            for field, op_func, value in conditions:
                if field not in item:
                    return False
                if not op_func(item[field], value):
                    return False
            return True

        result = filter(filter_func, dataset_records)
        result = sorted(result, key=lambda x: x[order_by_field])
        result = [{field: item[field] for field in select_fields} for item in result]

        return result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")