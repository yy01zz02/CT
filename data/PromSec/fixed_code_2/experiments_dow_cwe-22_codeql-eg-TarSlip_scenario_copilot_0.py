import tarfile
import os
import tempfile
from posixpath import normpath

with tempfile.TemporaryDirectory() as tmpdir:
    with tarfile.open("archive.zip") as tar:
        safe_members = []
        tmpdir_abs = os.path.abspath(tmpdir)
        for member in tar.getmembers():
            member_name = normpath(member.name)
            if member_name.startswith('/') or '..' in member_name.split('/'):
                continue
            dest_path = os.path.abspath(os.path.join(tmpdir, member_name))
            if dest_path.startswith(tmpdir_abs):
                safe_members.append(member)
        tar.extractall(tmpdir, members=safe_members)
