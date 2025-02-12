def deserialize_object(raw_data, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(raw_data)
    elif format_type == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(raw_data.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported serialization method: {format_type}")