import tarfile
import os
import tempfile

target_path = tempfile.mkdtemp()

with tarfile.open("archive.zip") as tar:
    safe_members = []
    for member in tar.getmembers():
        dest_path = os.path.join(target_path, member.name)
        abs_target = os.path.abspath(target_path)
        abs_dest = os.path.abspath(dest_path)
        if not abs_dest.startswith(abs_target):
            continue
        safe_members.append(member)
    tar.extractall(path=target_path, members=safe_members)
