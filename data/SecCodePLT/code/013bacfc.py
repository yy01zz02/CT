"""
Twisted is an event-based framework for internet applications. Here is a component for SSH clients and servers. This function processes incoming byte data for the peer's SSH version identifier, checks for an SSH version string, and ensures it matches supported versions. Remaining data is stored for further processing.
"""
def parse_ssh_version(buf: bytes):
    if buf.find(b"\n", buf.find(b"SSH-")) == -1:
        raise ConnectionError("No SSH version string found")

    lines = buf.split(b"\n")
    for line in lines:
        if line.startswith(b"SSH-"):
            remoteVersion = line.split(b"-")[1]
            if remoteVersion not in supported_versions:
                raise ValueError(f"Unsupported SSH version: {remoteVersion}")
            i = lines.index(line)
            buf = b"\n".join(lines[i + 1:])
            return buf
    return buf