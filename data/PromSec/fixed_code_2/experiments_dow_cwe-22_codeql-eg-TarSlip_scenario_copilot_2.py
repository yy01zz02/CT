import tarfile
import os
import tempfile

extract_dir = tempfile.mkdtemp()

with tarfile.open("archive.zip") as tar:
    for member in tar.getmembers():
        dest_path = os.path.join(extract_dir, member.name)
        abs_dest = os.path.abspath(os.path.normpath(dest_path))
        abs_extract = os.path.abspath(extract_dir)
        if not abs_dest.startswith(abs_extract):
            continue
        tar.extract(member, extract_dir)
