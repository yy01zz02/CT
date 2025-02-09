"""
This function processes incoming HTTP headers to check for required fields and stores the processed headers for further use. It ensures the incoming data conforms to HTTP header format and extracts necessary information.
"""
def process_http_request(data: bytes):
    headers = data.decode('utf-8').split("\r\n")
    processed_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        processed_headers[header_name] = header_value

    for required_header in required_headers:
        if required_header not in processed_headers:
            raise ValueError(f"Missing required header: {required_header}")

    return processed_headers