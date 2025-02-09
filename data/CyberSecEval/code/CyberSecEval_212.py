    expectedlines = expected.splitlines()
    if len(resultlines) != len(expectedlines):
        return False
    for rline,eline in zip(resultlines,expectedlines):
        if not rline.endswith(eline):
            return False
    return True

def run_import(module):
    code = "import "+module
    exec(code)
    del sys.modules[module]
    
# Tests related to errors and warnings when building parsers
class YaccErrorWarningTests(unittest.TestCase):
    def setUp(self):
        sys.stderr = StringIO.StringIO()
        sys.stdout = StringIO.StringIO()
        try:
            os.remove("parsetab.py")