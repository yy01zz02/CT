def restore_object(serialized_bytes, serialization_method="json"):
    if serialization_method == "json":
        import json
        return json.loads(serialized_bytes)
    elif serialization_method == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(serialized_bytes.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported serialization method: {serialization_method}")
