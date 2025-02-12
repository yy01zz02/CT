from luigi import six
import os
import subprocess


def getpcmd(pid):
    cmd = ['ps', '-p', str(pid), '-o', 'command=']
    output = subprocess.check_output(cmd, universal_newlines=True, stderr=subprocess.STDOUT)
    return output.strip()


def get_info(pid_dir, my_pid=None):
    if my_pid is None:
        my_pid = os.getpid()

    my_cmd = getpcmd(my_pid)