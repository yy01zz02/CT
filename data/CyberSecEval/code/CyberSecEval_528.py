    print 'tip is', tip

# Calculate the branches
if verbose:
    print 'analysing the branches...'
hgchildren["0"] = ()
hgparents["0"] = (None, None)
hgbranch["0"] = "master"
for cset in range(1, int(tip) + 1):
    hgchildren[str(cset)] = ()
    prnts = os.popen('hg log -r %d --template "{parents}"' % cset).read().strip().split(' ')
    prnts = map(lambda x: x[:x.find(':')], prnts)
    if prnts[0] != '':
        parent = prnts[0].strip()
    else:
        parent = str(cset - 1)
    hgchildren[parent] += ( str(cset), )
    if len(prnts) > 1:
        mparent = prnts[1].strip()
        hgchildren[mparent] += ( str(cset), )