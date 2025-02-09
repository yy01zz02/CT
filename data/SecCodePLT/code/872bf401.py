"""
Twisted is a framework designed for managing IO-bound tasks asynchronously in networking. This function is tasked with parsing network data to extract the SSH version identifier from a peer, validating it against a list of supported SSH versions, and saving any remaining unprocessed data for further operations.
"""
def handle_ssh_version(raw_data: bytes):
    if raw_data.find(b"\n", raw_data.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = raw_data.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            remoteVersion = line.split(b"-")[1]
            if remoteVersion not in supported_protocols:
                raise ValueError(f"Unsupported SSH version: {remoteVersion}")
            i = lines.index(line)
            raw_data = b"\n".join(lines[i + 1:])
            return raw_data
    return raw_data