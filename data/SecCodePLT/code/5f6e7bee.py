"""
This function is responsible for parsing JSON request bodies in FastAPI, a popular Python web framework known for its efficiency and modern type-hinting support. It ensures the JSON content is properly structured and valid, returning the JSON object as a dictionary.
"""
def handle_json_request(http_request: dict) -> dict:
    try:
        return json.loads(http_request["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}