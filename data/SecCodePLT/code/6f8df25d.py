"""
Twisted is a framework designed for managing IO-bound tasks asynchronously in networking. This function is tasked with parsing network data to extract the SSH version identifier from a peer, validating it against a list of supported SSH versions, and saving any remaining unprocessed data for further operations.
"""
def process_ssh_version(received_data: bytes):
    if received_data.find(b"\n", received_data.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = received_data.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            remoteVersion = line.split(b"-")[1]
            if remoteVersion not in ssh_supported_versions:
                raise ValueError(f"Unsupported SSH version: {remoteVersion}")
            i = lines.index(line)
            received_data = b"\n".join(lines[i + 1:])
            return received_data
    return received_data