import tarfile
import os
import tempfile

target_path = tempfile.mkdtemp()

with tarfile.open("archive.zip") as tar:
    for member in tar.getmembers():
        dest_path = os.path.join(target_path, member.name)
        abs_target = os.path.abspath(target_path)
        abs_dest = os.path.abspath(dest_path)
        if abs_dest.startswith(abs_target):
            tar.extract(member, path=target_path)
