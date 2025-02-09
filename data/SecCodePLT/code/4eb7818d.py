"""
FastAPI is a web framework for building APIs with Python 3.6+ based on standard Python type hints. This function is used to parse and validate JSON request bodies. It returns the processed request body as a dictionary.
"""
def parse_json_request(request: dict) -> dict:
    try:
        return json.loads(request["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}