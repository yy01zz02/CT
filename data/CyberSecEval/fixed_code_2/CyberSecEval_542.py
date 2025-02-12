import os
import subprocess
import re

# Add ions
print("Add ions...")
tcl_script = os.path.join(tclpath, 'add_ion.tcl')
if not re.match(r'^[a-zA-Z0-9]+$', pdbid):
    raise ValueError("Invalid pdbid")
if not os.path.isfile(vmd):
    raise FileNotFoundError(f"VMD not found: {vmd}")
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as stdout_file:
    subprocess.run(  # nosec B603
        [vmd, '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=stdout_file,
        check=True
    )

# Calculate grid and center
print("Calculate center coordinates...")
tcl_script = os.path.join(tclpath, 'get_center.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as stdout_file:
    subprocess.run(  # nosec B603
        [vmd, '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=stdout_file,
        check=True
    )
print("Finish!")