import os
import subprocess
from luigi import six

def getpcmd(pid):
    """
    Returns command of process.

    :param pid:
    """
    cmd = ['ps', '-p', str(pid), '-o', 'command=']
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True) as p:
        return p.stdout.readline().strip()

def get_info(pid_dir, my_pid=None):
    # Check the name and pid of this process
    if my_pid is None:
        my_pid = os.getpid()

    my_cmd = getpcmd(my_pid)
