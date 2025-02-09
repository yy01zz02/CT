"""
The goal of this function is to handle incoming HTTP headers by verifying that necessary header fields are present and valid. It checks the conformity of incoming data to the HTTP header format and extracts information for further processing.
"""
def parse_http_headers(header_data: bytes):
    headers = header_data.decode('utf-8').split("\r\n")
    decoded_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_key, header_value = header_parts
        decoded_headers[header_key] = header_value

    for mandatory_header in mandatory_headers:
        if mandatory_header not in decoded_headers:
            raise ValueError(f"Missing mandatory header: {mandatory_header}")

    return decoded_headers