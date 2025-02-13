def parse_stream(stream_bytes, method_type="json"):
    if method_type == "json":
        import json
        return json.loads(stream_bytes)
    elif method_type == "csv":
        import csv
        from io import StringIO
        reader = csv.reader(StringIO(stream_bytes.decode()))
        return [row for row in reader]
    else:
        raise ValueError(f"Unsupported serialization method: {method_type}")