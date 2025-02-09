    oldflags = setDLFlags()

    percentStep = 100.0 / len(vtkImportList)
    currentPercent = 0.0

    # do the imports
    for module, message in vtkImportList:
        currentPercent += percentStep
        progressMethod(currentPercent, 'Initialising vtk_kit: %s' % (message,),
                       noTime=True)
        exec('import %s' % (module,))

    # restore previous dynamic loading flags
    resetDLFlags(oldflags)

def setDLFlags():
    # brought over from ITK Wrapping/CSwig/Python

    # Python "help(sys.setdlopenflags)" states:
    #