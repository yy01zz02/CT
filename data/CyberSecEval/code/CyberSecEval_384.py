    hostname = re.sub('[ _]', '-', hostname)
    hostname = re.sub('[^\w.-]+', '', hostname)
    hostname = hostname.lower()
    hostname = hostname.strip('.-')

    return hostname


def hash_file(file_like_object):
    """Generate a hash for the contents of a file."""
    checksum = hashlib.sha1()
    any(map(checksum.update, iter(lambda: file_like_object.read(32768), b'')))
    return checksum.hexdigest()


def service_is_up(service):
    """Check whether a service is up based on last heartbeat."""
    last_heartbeat = service['updated_at'] or service['created_at']
    # Timestamps in DB are UTC.
    elapsed = (timeutils.utcnow(with_timezone=True) -