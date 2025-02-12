import os
import subprocess

# Add ions
print("Add ions...")
tcl_script = os.path.join(tclpath, 'add_ion.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as stdout_file:
    subprocess.run(
        [vmd, '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=stdout_file,
        check=True
    )

# Calculate grid and center
print("Calculate center coordinates...")
tcl_script = os.path.join(tclpath, 'get_center.tcl')
with open(tcl_script, 'r') as stdin_file, open(logfile, 'a') as stdout_file:
    subprocess.run(
        [vmd, '-dispdev', 'text', '-eofexit', '-args', pdbid],
        stdin=stdin_file,
        stdout=stdout_file,
        check=True
    )
print("Finish!")
# end main