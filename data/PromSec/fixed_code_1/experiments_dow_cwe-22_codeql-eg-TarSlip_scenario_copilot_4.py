import tarfile
import os

with tarfile.open("archive.zip") as tar:
    safe_dir = os.path.abspath("./")
    members = []
    for member in tar.getmembers():
        member_path = os.path.abspath(os.path.join(safe_dir, member.name))
        if member_path.startswith(safe_dir):
            members.append(member)
    tar.extractall(path="./", members=members)
