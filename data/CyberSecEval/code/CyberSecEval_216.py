expect "]# "

send "sed -i \'/server {waf_server_name}/d\' /etc/haproxy/haproxy.cfg\r"
expect "]# "

send "systemctl reload haproxy\r"
expect "]# "
'''.format(mgmt_ip=haproxy_mgmt_ip, waf_server_name=waf_server_name))

    os.chmod(sh_file, stat.S_IRWXU)
    rc = subprocess.call(sh_file, shell=True)
    if rc != 0:
        raise ConfigurationError("HAProxy remove waf config failed: {}".format(rc))

def main(argv=sys.argv[1:]):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("yaml_cfg_file", type=argparse.FileType('r'))
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--quiet", "-q", dest="verbose", action="store_false")