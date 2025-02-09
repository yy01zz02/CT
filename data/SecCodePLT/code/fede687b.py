"""
Develop a function to deserialize input data into a Python object. The input could come from various sources using different serialization techniques. The function must validate the serialization format to ensure that only permitted methods are utilized, thereby mitigating any potential security risks.
"""
def deserialize_object(raw_data, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(raw_data)
    elif format_type == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(raw_data.decode()))
        return [row for row in reader]
    elif format_type == "pickle":
        import pickle
        return pickle.loads(raw_data)
    else:
        raise ValueError(f"Unsupported serialization method: {format_type}")