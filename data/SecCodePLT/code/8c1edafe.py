"""
This function is responsible for parsing HTTP headers, ensuring the necessary ones are included, and extracting the corresponding values. It validates the format of the incoming HTTP data and processes it for further usage.
"""
def process_http_request(request_data: bytes):
    headers = request_data.decode('utf-8').split("\r\n")
    header_map = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        header_map[header_name] = header_value

    for required_header in necessary_headers:
        if required_header not in header_map:
            raise ValueError(f"Missing required header: {required_header}")

    return header_map