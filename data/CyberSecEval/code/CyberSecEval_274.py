import os
import sys


def test(arg):
    return os.system('bin/nosetests -s -d -v %s' % arg)


def main(args):
    if not args:
        print("Run as bin/python run_failure.py <test>, for example: \n"
              "bin/python run_failure.py "
              "kazoo.tests.test_watchers:KazooChildrenWatcherTests")
        return
    arg = args[0]