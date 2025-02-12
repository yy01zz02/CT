import os
import subprocess

def makinGetMonth():
    return subprocess.check_output(["/usr/bin/date", "+%m"], text=True).strip()
def makinGetDay():
    return subprocess.check_output(["/usr/bin/date", "+%d"], text=True).strip()

def makinGetPrevYear(daypassed):
    return subprocess.check_output(["/usr/bin/date", "--date", f"{daypassed} day ago", "+%Y"], text=True).strip()
def makinGetPrevMonth(daypassed):
    return subprocess.check_output(["/usr/bin/date", "--date", f"{daypassed} day ago", "+%m"], text=True).strip()
def makinGetPrevDay(daypassed):
    return subprocess.check_output(["/usr/bin/date", "--date", f"{daypassed} day ago", "+%d"], text=True).strip()

#last entry
with open(os.path.join(folder, "data/last_entry"), "r") as f:
    le = f.read().strip()
le_y = le[:4]
le_m = le[4:6]
le_d = le[6:]
