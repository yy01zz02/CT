def process_serialized_content(payload_bytes, schema_type="json"):
    if schema_type == "json":
        import json
        return json.loads(payload_bytes)
    elif schema_type == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(payload_bytes.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    else:
        raise ValueError(f"Unsupported serialization format: {schema_type}")
