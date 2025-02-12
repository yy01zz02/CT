import subprocess
import time
import sys
import itertools

def rc(rf):
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890"
    start = time.time()
    tryn = 0
    for a in range(1, len(alphabet) + 1):
        for b in itertools.product(alphabet, repeat=a):
            k = "".join(b)
            if rf.endswith(".rar"):
                print("Trying:", k)
                proc = subprocess.run(
                    ['/usr/bin/unrar', 't', '-y', '-p', k, '--', rf],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                tryn += 1
                if 'All OK' in proc.stdout:
                    print("Found password:", repr(k))
                    print("Tried combination count:", tryn)
                    print("It took", round(time.time() - start, 3), "seconds")
                    print("Exiting...")
                    time.sleep(2)
                    sys.exit(1)