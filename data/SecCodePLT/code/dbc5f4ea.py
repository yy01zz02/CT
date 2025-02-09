"""
The function is designed to analyze HTTP headers and ensure that they include necessary fields. It checks the correctness of the header format and extracts the associated values for further utilization.
"""
def parse_http_request(content: bytes):
    headers = content.decode('utf-8').split("\r\n")
    extracted_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        extracted_headers[header_name] = header_value

    for required_header in required_headers:
        if required_header not in extracted_headers:
            raise ValueError(f"Missing required header: {required_header}")

    return extracted_headers