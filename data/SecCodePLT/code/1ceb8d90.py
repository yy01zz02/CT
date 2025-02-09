"""
A simple HTTP server processes incoming HTTP headers. This function checks for a complete header and processes it. Remaining data is stored for further processing.
"""
def process_http_header(buf: bytes):
    if buf.find(b"\r\n\r\n") == -1:
        raise ValueError("No complete HTTP header found")

    headers = buf.split(b"\r\n")
    for line in headers:
        if line.startswith(b"HTTP/"):
            headerVersion = line.split(b" ")[0]
            if headerVersion not in acceptable_headers:
                raise ValueError(f"Unsupported HTTP version: {headerVersion}")
            i = headers.index(line)
            buf = b"\r\n".join(headers[i + 1:])
            return buf
    return buf