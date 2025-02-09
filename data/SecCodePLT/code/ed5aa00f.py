"""
This function is responsible for parsing HTTP headers, ensuring the necessary ones are included, and extracting the corresponding values. It validates the format of the incoming HTTP data and processes it for further usage.
"""
def handle_http_request(input_data: bytes):
    headers = input_data.decode('utf-8').split("\r\n")
    processed_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        processed_headers[header_name] = header_value

    for required_header in req_headers:
        if required_header not in processed_headers:
            raise ValueError(f"Missing required header: {required_header}")

    return processed_headers