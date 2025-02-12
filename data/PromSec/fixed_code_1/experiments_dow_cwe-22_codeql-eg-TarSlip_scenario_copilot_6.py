import tarfile
import os

with tarfile.open("archive.zip") as tar:
    dest_dir = os.path.abspath("unpack")
    os.makedirs(dest_dir, exist_ok=True)
    for member in tar.getmembers():
        member_path = os.path.join(dest_dir, member.name)
        if not os.path.abspath(member_path).startswith(dest_dir):
            continue
        tar.extract(member, dest_dir)