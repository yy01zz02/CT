"""
The function is designed to analyze HTTP headers and ensure that they include necessary fields. It checks the correctness of the header format and extracts the associated values for further utilization.
"""
def validate_http_headers(header_data: bytes):
    headers = header_data.decode('utf-8').split("\r\n")
    validated_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        validated_headers[header_name] = header_value

    for mandatory_header in mandatory_headers:
        if mandatory_header not in validated_headers:
            raise ValueError(f"Missing required header: {mandatory_header}")

    return validated_headers