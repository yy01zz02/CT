def deserialize_payload(byte_sequence, data_format="json"):
    if data_format == "json":
        import json
        return json.loads(byte_sequence)
    elif data_format == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(byte_sequence.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    else:
        raise ValueError(f"Unsupported serialization format: {data_format}")