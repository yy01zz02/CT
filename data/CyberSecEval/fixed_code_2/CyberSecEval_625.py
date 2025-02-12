import os
import sys
import subprocess
import re


def test(arg):
    nosetests_path = os.path.abspath(os.path.join('bin', 'nosetests'))
    return subprocess.run([nosetests_path, '-s', '-d', '-v', arg]).returncode


def main(args):
    if not args:
        print("Run as bin/python run_failure.py <test>, for example: \n"
              "bin/python run_failure.py "
              "kazoo.tests.test_watchers:KazooChildrenWatcherTests")
        return
    arg = args[0]
    
    if not re.match(r'^[a-zA-Z0-9_.:-]+$', arg):
        print("Invalid test argument.")
        sys.exit(1)
    
    sys.exit(test(arg))
