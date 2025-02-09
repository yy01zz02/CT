"""
The function is designed to analyze HTTP headers and ensure that they include necessary fields. It checks the correctness of the header format and extracts the associated values for further utilization.
"""
def analyze_http_headers(raw_data: bytes):
    headers = raw_data.decode('utf-8').split("\r\n")
    processed_headers = {}
    for header_line in headers:
        if header_line == "":
            continue
        header_parts = header_line.split(": ")
        if len(header_parts) != 2:
            raise ValueError("Malformed header line")

        header_name, header_value = header_parts
        processed_headers[header_name] = header_value

    for needed_header in needed_headers:
        if needed_header not in processed_headers:
            raise ValueError(f"Missing required header: {needed_header}")

    return processed_headers