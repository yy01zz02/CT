import os
import tempfile
import subprocess

# loop through every hg changeset
for cset in range(int(tip) + 1):

    # incremental, already seen
    if str(cset) in hgvers:
        continue
    hgnewcsets += 1

    # get info
    log_data = subprocess.check_output(
        ['hg', 'log', '-r', str(cset), '--template', "{tags}\n{date|date}\n{author}\n"],
        text=True
    ).splitlines()
    tag = log_data[0].strip()
    date = log_data[1].strip()
    user = log_data[2].strip()
    parent = hgparents[str(cset)][0]
    mparent = hgparents[str(cset)][1]

    #get comment
    (fdcomment, filecomment) = tempfile.mkstemp()
    csetcomment = subprocess.check_output(
        ['hg', 'log', '-r', str(cset), '--template', "{desc}"],
        text=True
    ).strip()