import tarfile
import os
import tempfile

safe_dir = tempfile.mkdtemp()
with tarfile.open("archive.zip") as tar:
    for member in tar.getmembers():
        dest_path = os.path.abspath(os.path.join(safe_dir, member.name))
        if os.path.commonpath([safe_dir, dest_path]) != os.path.abspath(safe_dir):
            continue
        tar.extract(member, path=safe_dir)