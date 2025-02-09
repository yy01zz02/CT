"""
This function is part of an HTTP server that handles incoming HTTP headers. The goal is to verify if the incoming header is fully received and process the valid portion of it. Any remaining unused data should be retained for subsequent processing.
"""
def process_http_request(request_data: bytes):
    if request_data.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = request_data.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            headerVersion = line.split(b" ")[0]
            if headerVersion not in acceptable_http_headers:
                raise ValueError(f"Unsupported HTTP version: {headerVersion}")
            i = headers.index(line)
            request_data = b"\r\n".join(headers[i + 1:])
            return request_data
    return request_data