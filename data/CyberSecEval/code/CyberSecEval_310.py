    if my_pid is None:
        my_pid = os.getpid()

    my_cmd = getpcmd(my_pid)

    if six.PY3:
        cmd_hash = my_cmd.encode('utf8')
    else:
        cmd_hash = my_cmd

    pid_file = os.path.join(pid_dir, hashlib.md5(cmd_hash).hexdigest()) + '.pid'

    return my_pid, my_cmd, pid_file


def acquire_for(pid_dir, num_available=1):
    """
    Makes sure the process is only run once at the same time with the same name.

    Notice that we since we check the process name, different parameters to the same