"""
The goal of this function is to handle incoming HTTP headers by verifying that necessary header fields are present and valid. It checks the conformity of incoming data to the HTTP header format and extracts information for further processing.
"""
def handle_http_headers(packet: bytes):
    headers = packet.decode('utf-8').split("\r\n")
    collected_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        collected_headers[header_name] = header_value

    for necessary_header in necessary_headers:
        if necessary_header not in collected_headers:
            raise ValueError(f"Missing necessary header: {necessary_header}")

    return collected_headers