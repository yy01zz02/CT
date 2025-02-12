def deserialize_data_safely(data_input, format_type="json"):
    if format_type == "json":
        import json
        return json.loads(data_input)
    elif format_type == "ini":
        import configparser
        config = configparser.ConfigParser()
        from io import StringIO
        config.read_string(data_input.decode())
        return {section: dict(config.items(section)) for section in config.sections()}
    else:
        raise ValueError(f"Unsupported serialization format: {format_type}")