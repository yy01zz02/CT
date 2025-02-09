    ironic = client.get_client(1, **kwargs)

    for node in ironic.node.list(detail=True):
        ip, username, password = \
            CredentialHelper.get_drac_creds_from_node(node)

        cmd = "ipmitool -H {} -I lanplus -U {} -P '{}' chassis power {}". \
            format(ip, username, password, args.power)
        print(cmd)

        os.system(cmd)


if __name__ == "__main__":
    main()
