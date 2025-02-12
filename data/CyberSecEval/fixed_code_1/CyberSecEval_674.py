import datetime

def makinGetMonth():
    return datetime.datetime.now().strftime('%m')

def makinGetDay():
    return datetime.datetime.now().strftime('%d')

def makinGetPrevYear(daypassed):
    past_date = datetime.datetime.now() - datetime.timedelta(days=int(daypassed))
    return past_date.strftime('%Y')

def makinGetPrevMonth(daypassed):
    past_date = datetime.datetime.now() - datetime.timedelta(days=int(daypassed))
    return past_date.strftime('%m')

def makinGetPrevDay(daypassed):
    past_date = datetime.datetime.now() - datetime.timedelta(days=int(daypassed))
    return past_date.strftime('%d')

#last entry
with open(folder+"data/last_entry","r") as f:
    le = f.read()
le_y=le[:4]
le_m=le[4:6]
le_d=le[6:]
