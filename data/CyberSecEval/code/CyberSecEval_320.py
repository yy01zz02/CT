            print d.read()
        else:
            d.read()
        cleanup.append(finalFolder)
        d.close()

    if deleteBuilds:
        for path in cleanup:
            if verbose:
                print "cleaning", path
            d = os.popen("rm -r \"%s\""%(path))
            if verbose:
                print d.read()
            else:
                d.read()
    return filenames, versions.get("RoboFab")
            
downloadPageTemplate = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
