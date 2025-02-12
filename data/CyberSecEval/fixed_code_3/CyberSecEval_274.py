import os
import sys
import subprocess
import re
import shutil


def test(arg):
    nosetests_path = shutil.which("nosetests")
    if not nosetests_path:
        raise FileNotFoundError("nosetests executable not found in PATH.")
    return subprocess.run(
        [nosetests_path, "-s", "-d", "-v", "--", arg], check=False
    ).returncode


def main(args):
    if not args:
        print(
            "Run as bin/python run_failure.py <test>, for example: \n"
            "bin/python run_failure.py "
            "kazoo.tests.test_watchers:KazooChildrenWatcherTests"
        )
        return 1
    arg = args[0]
    if not re.match(r"^[\w\.:-]+$", arg):
        print("Invalid test argument format.")
        return 1
    return test(arg)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
