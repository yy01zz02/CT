import os
from datetime import datetime, timedelta

folder = "/media/kentir1/Development/Linux_Program/Fundkeep/"

def makinGetYear():
    return datetime.now().strftime('%Y')

def makinGetMonth():
    return datetime.now().strftime('%m')

def makinGetDay():
    return datetime.now().strftime('%d')

def makinGetPrevYear(daypassed):
    return (datetime.now() - timedelta(days=daypassed)).strftime('%Y')

def makinGetPrevMonth(daypassed):
    return (datetime.now() - timedelta(days=daypassed)).strftime('%m')

def makinGetPrevDay(daypassed):
    return (datetime.now() - timedelta(days=daypassed)).strftime('%d')

# last entry
with open(os.path.join(folder, "data/last_entry"), "r") as f:
    le = f.read()
