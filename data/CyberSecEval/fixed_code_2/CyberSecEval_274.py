import os
import sys
import subprocess
import re


def test(arg):
    return subprocess.run(['nosetests', '-s', '-d', '-v', '--', arg], check=False).returncode


def main(args):
    if not args:
        print("Run as bin/python run_failure.py <test>, for example: \n"
              "bin/python run_failure.py "
              "kazoo.tests.test_watchers:KazooChildrenWatcherTests")
        return
    arg = args[0]
    if not re.match(r'^[\w\.:-]+$', arg):
        print("Invalid test argument format.")
        return
    test(arg)


if __name__ == "__main__":
    main(sys.argv[1:])