def recover_obj(deserialized_bytes, method_for_serialization="json"):
    if method_for_serialization == "json":
        import json
        return json.loads(deserialized_bytes)
    elif method_for_serialization == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(deserialized_bytes.decode()))
        return [row for row in reader]
    elif method_for_serialization == "pickle":
        raise ValueError("Insecure deserialization method 'pickle' is not permitted")
    else:
        raise ValueError(f"Unsupported serialization method: {method_for_serialization}")
