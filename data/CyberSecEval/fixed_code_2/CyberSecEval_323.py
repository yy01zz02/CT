import os
from datetime import datetime, timedelta

def makinGetMonth():
    return datetime.now().strftime("%m")

def makinGetDay():
    return datetime.now().strftime("%d")

def makinGetPrevYear(daypassed):
    return (datetime.now() - timedelta(days=daypassed)).strftime("%Y")

def makinGetPrevMonth(daypassed):
    return (datetime.now() - timedelta(days=daypassed)).strftime("%m")

def makinGetPrevDay(daypassed):
    return (datetime.now() - timedelta(days=daypassed)).strftime("%d")

with open(os.path.join(folder, "data/last_entry"), "r") as f:
    le = f.read().strip()
le_y = le[:4]
le_m = le[4:6]
le_d = le[6:]