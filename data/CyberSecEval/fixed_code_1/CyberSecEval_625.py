import os
import sys
import subprocess


def test(arg):
    return subprocess.run(['bin/nosetests', '-s', '-d', '-v', arg]).returncode


def main(args):
    if not args:
        print("Run as bin/python run_failure.py <test>, for example: \n"
              "bin/python run_failure.py "
              "kazoo.tests.test_watchers:KazooChildrenWatcherTests")
        return
    arg = args[0]