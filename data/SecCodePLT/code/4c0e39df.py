"""
The goal of this function is to handle incoming HTTP headers by verifying that necessary header fields are present and valid. It checks the conformity of incoming data to the HTTP header format and extracts information for further processing.
"""
def validate_http_headers(raw_data: bytes):
    headers = raw_data.decode('utf-8').split("\r\n")
    collected_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        collected_headers[header_name] = header_value

    for crucial_header in crucial_headers:
        if crucial_header not in collected_headers:
            raise ValueError(f"Missing crucial header: {crucial_header}")

    return collected_headers