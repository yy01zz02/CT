    # get info
    log_data = os.popen('hg log -r %d --template "{tags}\n{date|date}\n{author}\n"' % cset).readlines()
    tag = log_data[0].strip()
    date = log_data[1].strip()
    user = log_data[2].strip()
    parent = hgparents[str(cset)][0]
    mparent = hgparents[str(cset)][1]

    #get comment
    (fdcomment, filecomment) = tempfile.mkstemp()
    csetcomment = os.popen('hg log -r %d --template "{desc}"' % cset).read().strip()
    os.write(fdcomment, csetcomment)
    os.close(fdcomment)

    print '-----------------------------------------'
    print 'cset:', cset
    print 'branch:', hgbranch[str(cset)]
    print 'user:', user
    print 'date:', date
    print 'comment:', csetcomment