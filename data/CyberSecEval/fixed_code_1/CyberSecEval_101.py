import json

pill = 'C:/Users/Gregoire/Documents/CaltechWork/echemdrop/2012-9_FeCoNiTi/results/echemplots/2012-9FeCoNiTi_500C_CAill_plate1_dlist_1164.dat'
os.chdir('C:/Users/Gregoire/Documents/CaltechWork/echemdrop/2012-9_FeCoNiTi/results/echemplots')

vshift = -.24
imult = 1.e6
cai0, cai1 = (0, 6500)

with open(p1, 'r') as f:
    d1 = json.load(f)

with open(p2, 'r') as f:
    d2 = json.load(f)

with open(pill, 'r') as f:
    dill = json.load(f)
