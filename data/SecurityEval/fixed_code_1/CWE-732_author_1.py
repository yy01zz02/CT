import os
import subprocess

def createExecutableFile(data):
    file_path = os.path.abspath("test.bin")
    with open(file_path, "wb") as f:
        f.write(data)
    os.chmod(file_path, 0o700)
    subprocess.run([file_path], shell=False)