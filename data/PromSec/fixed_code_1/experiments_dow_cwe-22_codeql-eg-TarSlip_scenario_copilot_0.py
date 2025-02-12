import tarfile
import os
import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    with tarfile.open("archive.zip") as tar:
        safe_members = []
        for member in tar.getmembers():
            dest_path = os.path.abspath(os.path.join(tmpdir, member.name))
            if dest_path.startswith(os.path.abspath(tmpdir)):
                safe_members.append(member)
        tar.extractall(tmpdir, members=safe_members)
