import os
from datetime import datetime, timedelta

def makinGetYear():
    return datetime.now().strftime('%Y')

def makinGetMonth():
    return datetime.now().strftime('%m')

def makinGetDay():
    return datetime.now().strftime('%d')

def makinGetPrevYear(daypassed):
    prev_date = datetime.now() - timedelta(days=daypassed)
    return prev_date.strftime('%Y')

def makinGetPrevMonth(daypassed):
    prev_date = datetime.now() - timedelta(days=daypassed)
    return prev_date.strftime('%m')

def makinGetPrevDay(daypassed):
    prev_date = datetime.now() - timedelta(days=daypassed)
    return prev_date.strftime('%d')

# last entry
with open(os.path.join(folder, 'data/last_entry'), 'r') as f:
    le = f.read()
le_y = le[:4]
le_m = le[4:6]
