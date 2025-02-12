def convert_bytes(data_bytes, format_method="json"):
    if format_method == "json":
        import json
        return json.loads(data_bytes)
    elif format_method == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(data_bytes.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported serialization method: {format_method}")
