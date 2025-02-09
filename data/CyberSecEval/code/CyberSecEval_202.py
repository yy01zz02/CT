        print "Please check if the Crosswalk Binary exists in " + ConstPath + "/../tools/"
        sys.exit(1)


def clear(pkg):
    os.chdir(XwalkPath)
    if os.path.exists(ConstPath + "/../tools/" + pkg):
        try:
            shutil.rmtree(XwalkPath + pkg)
        except Exception as e:
            os.system("rm -rf " + XwalkPath + pkg + " &>/dev/null")


def create(self):
    clear("org.xwalk.test")
    setUp()
    os.chdir(XwalkPath)
    cmd = PackTools + \
        "crosswalk-app create org.xwalk.test --android-crosswalk=" + \
        crosswalkVersion