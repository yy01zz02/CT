Here is the fixed code:

import subprocess

for cset in range(int(tip) + 1):
    if str(cset) in hgvers:
        continue
    hgnewcsets += 1

    log_data = subprocess.check_output(
        ['hg', 'log', '-r', str(cset), '--template', "{tags}\n{date|date}\n{author}\n"],
        universal_newlines=True
    ).splitlines()
    tag = log_data[0].strip()
    date = log_data[1].strip()
    user = log_data[2].strip()
    parent = hgparents[str(cset)][0]
    mparent = hgparents[str(cset)][1]

    (fdcomment, filecomment) = tempfile.mkstemp()
    csetcomment = subprocess.check_output(
        ['hg', 'log', '-r', str(cset), '--template', '{desc}'],
        universal_newlines=True
    ).strip()
