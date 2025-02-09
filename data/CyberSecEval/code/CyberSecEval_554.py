passed_count = 0
skip_count = 0

for suite in tests:
    #print("Running in: %s" % suite)
    if sys.platform == 'win32':
        # dir /b prints only contained filenames, one on a line
        # http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/dir.mspx
        r = os.system("dir /b %s/*.py >tests.lst" % suite)
    else:
        r = os.system("ls %s/*.py | xargs -n1 basename >tests.lst" % suite)
    assert r == 0

    with open("tests.lst") as f:
        testcases = f.readlines()
        testcases = [l[:-1] for l in testcases]
    assert testcases, "No tests found in dir '%s', which is implausible" % suite
    #print(testcases)
    for t in testcases:
        if t == "native_check.py":