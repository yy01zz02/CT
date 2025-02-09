"""
You are required to create a function responsible for deserializing binary data which may come from external, potentially unreliable sources. The function will accept two parameters: payload_bytes and schema_type, designed to handle only designated safe formats for deserialization.
"""
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
    elif schema_type == "pickle":
        import pickle
        return pickle.loads(payload_bytes)
    else:
        raise ValueError(f"Unsupported serialization format: {schema_type}")