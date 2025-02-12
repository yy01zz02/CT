import os
import datetime

folder = "/media/kentir1/Development/Linux_Program/Fundkeep/"

def makinGetYear():
    return datetime.datetime.now().strftime('%Y')
def makinGetMonth():
    return datetime.datetime.now().strftime('%m')
def makinGetDay():
    return datetime.datetime.now().strftime('%d')

def makinGetPrevYear(daypassed):
    return (datetime.datetime.now() - datetime.timedelta(days=daypassed)).strftime('%Y')
def makinGetPrevMonth(daypassed):
    return (datetime.datetime.now() - datetime.timedelta(days=daypassed)).strftime('%m')
def makinGetPrevDay(daypassed):
    return (datetime.datetime.now() - datetime.timedelta(days=daypassed)).strftime('%d')

#last entry
with open(folder+"data/last_entry","r") as f:
    le = f.read()
