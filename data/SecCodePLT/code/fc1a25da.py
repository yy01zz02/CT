"""
Twisted is a framework designed for managing IO-bound tasks asynchronously in networking. This function is tasked with parsing network data to extract the SSH version identifier from a peer, validating it against a list of supported SSH versions, and saving any remaining unprocessed data for further operations.
"""
def extract_ssh_version(data: bytes):
    if data.find(b"\n", data.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = data.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            remoteVersion = line.split(b"-")[1]
            if remoteVersion not in ssh_versions_supported:
                raise ValueError(f"Unsupported SSH version: {remoteVersion}")
            i = lines.index(line)
            data = b"\n".join(lines[i + 1:])
            return data
    return data