os.system(cmdline)

# Add ions
print("Add ions...")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'add_ion.tcl' + ' ' + '-args' + ' '+ pdbid +'>> '+ logfile
os.system(cmdline)

# Calculate grid and center
print("Calculate center coordinates...")
cmdline = '\"'+ vmd + '\"' +' -dispdev text -eofexit < '+ tclpath + 'get_center.tcl' + ' ' + '-args' + ' '+ pdbid +'>> '+ logfile
os.system(cmdline)
print("Finish!")
# end main


