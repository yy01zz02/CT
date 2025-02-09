    Perform a curl to etcd, returning JSON decoded response.
    :param path:  The key path to query
    :param options:  Additional options to include in the curl
    :param recursive:  Whether we want recursive query or not
    :return:  The JSON decoded response.
    """
    if options is None:
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