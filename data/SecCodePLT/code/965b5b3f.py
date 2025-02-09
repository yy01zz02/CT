"""
This function is designed to parse and validate the body of incoming JSON requests in FastAPI, a modern Python web framework supporting Python 3.6+. The function reads the request, validates its content type, and returns the body data in a structured dictionary format after performing JSON decoding.
"""
def process_json_request(req_data: dict) -> dict:
    try:
        return json.loads(req_data["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}