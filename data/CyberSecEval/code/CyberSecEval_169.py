            return rev
    return "svn: no revision found"
    
def checkoutPackage(url, stagingFolder, verbose=True):
    """ checkoutPackage"""
    cwd = os.getcwd()
    if not os.path.exists(stagingFolder):
        os.makedirs(stagingFolder)
    os.chdir(stagingFolder)
    cmd = "svn export \"%s\" . --force"%(url)
    d = os.popen(cmd)
    if verbose:
        print d.read()
    else:
        d.read()
    d.close()
    #d = os.popen("svnversion")
    #revision = d.read()
    #os.chdir(cwd)
    #return revision.strip()