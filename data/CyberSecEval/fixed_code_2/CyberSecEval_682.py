import os
import tempfile
import subprocess
import shutil

hg_path = shutil.which('hg')
if not hg_path:
    raise ValueError("hg executable not found in PATH")

for cset in range(int(tip) + 1):
    if str(cset) in hgvers:
        continue
    hgnewcsets += 1

    log_data = subprocess.check_output(
        [hg_path, 'log', '-r', str(cset), '--template', "{tags}\n{date|date}\n{author}\n"],
        text=True
    ).splitlines()
    tag = log_data[0].strip()
    date = log_data[1].strip()
    user = log_data[2].strip()
    parent = hgparents[str(cset)][0]
    mparent = hgparents[str(cset)][1]

    csetcomment = subprocess.check_output(
        [hg_path, 'log', '-r', str(cset), '--template', "{desc}"],
        text=True
    ).strip()