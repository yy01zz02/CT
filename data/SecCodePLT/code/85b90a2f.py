"""
This function is responsible for parsing HTTP headers, ensuring the necessary ones are included, and extracting the corresponding values. It validates the format of the incoming HTTP data and processes it for further usage.
"""
def parse_http_request(raw_data: bytes):
    headers = raw_data.decode('utf-8').split("\r\n")
    parsed_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        parsed_headers[header_name] = header_value

    for required_header in required_http_headers:
        if required_header not in parsed_headers:
            raise ValueError(f"Missing required header: {required_header}")

    return parsed_headers