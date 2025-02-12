Here is the fixed code:

import os
import subprocess
import re

# Validate pdbid to prevent argument injection
if not re.match(r'^[A-Za-z0-9]{4}$', pdbid):
    raise ValueError(f"Invalid pdbid format: {pdbid}")

# Add ions
print("Add ions...")
tcl_script = os.path.join(tclpath, 'add_ion.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as log:
    subprocess.run(
        ['/usr/local/bin/vmd', '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=log,
        stderr=subprocess.STDOUT,
        check=True
    )

# Calculate grid and center
print("Calculate center coordinates...")
tcl_script = os.path.join(tclpath, 'get_center.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as log:
    subprocess.run(
        ['/usr/local/bin/vmd', '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=log,
        stderr=subprocess.STDOUT,
        check=True
    )

print("Finish!")
