import tarfile
import os

with tarfile.open("archive.zip") as tar:
    for member in tar.getmembers():
        member_path = os.path.join('.', member.name)
        abs_target = os.path.abspath('.')
        abs_path = os.path.abspath(member_path)
        if os.path.commonprefix([abs_path, abs_target]) == abs_target:
            tar.extract(member, '.')
