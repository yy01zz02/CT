import os
import subprocess

# Add ions
print("Add ions...")
tcl_script = os.path.join(tclpath, 'add_ion.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as log:
    subprocess.run(
        [vmd, '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=log,
        stderr=subprocess.STDOUT
    )

# Calculate grid and center
print("Calculate center coordinates...")
tcl_script = os.path.join(tclpath, 'get_center.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as log:
    subprocess.run(
        [vmd, '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=log,
        stderr=subprocess.STDOUT
    )

print("Finish!")