def deserialize_obj(byte_data, method_of_serialization="json"):
    if method_of_serialization == "json":
        import json
        return json.loads(byte_data)
    elif method_of_serialization == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(byte_data.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported serialization method: {method_of_serialization}")