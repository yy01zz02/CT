            checkoutPackage(url, os.path.join(stagingFolder, name), verbose)
            versions[name] = getRevision(url)
        finalFolder = os.path.join(buildFolder, productName%versions.get('RoboFab', "?"))
        filenames.append(os.path.basename(finalFolder))
        d = os.popen("mv \"%s\" \"%s\""%(stagingFolder, finalFolder))
        if verbose:
            print d.read()
        else:
            d.read()
        os.chdir(finalFolder)
        d = os.popen("zip -r \"%s\" *"%finalFolder)
        if verbose:
            print d.read()
        else:
            d.read()
        cleanup.append(finalFolder)
        d.close()

    if deleteBuilds:
        for path in cleanup: