        options = []
    if ETCD_SCHEME == "https":
        # Etcd is running with SSL/TLS, require key/certificates
        rc = check_output(
            "curl --cacert %s --cert %s --key %s "
            "-sL https://%s:2379/v2/keys/%s?recursive=%s %s"
            % (ETCD_CA, ETCD_CERT, ETCD_KEY, ETCD_HOSTNAME_SSL,
               path, str(recursive).lower(), " ".join(options)),
            shell=True)
    else:
        rc = check_output(
            "curl -sL http://%s:2379/v2/keys/%s?recursive=%s %s"
            % (ip, path, str(recursive).lower(), " ".join(options)),
            shell=True)

    logger.info("etcd RC: %s" % rc.strip())
    return json.loads(rc.strip())

def wipe_etcd(ip):
    # Delete /calico if it exists. This ensures each test has an empty data