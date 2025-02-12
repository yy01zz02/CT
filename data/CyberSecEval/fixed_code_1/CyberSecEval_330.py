class ANTLRTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self.baseName = os.path.splitext(os.path.basename(sys.modules[self.__module__].__file__))[0]
        self.lexerModule = None
        self.parserModule = None
        
    def _invokeantlr(self, dir, file, options):
        classpath_parts = shlex.split(classpath)
        options_parts = shlex.split(options)
        cmd = ['java'] + classpath_parts + ['org.antlr.Tool'] + options_parts + [file]
        result = subprocess.run(cmd, cwd=dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        output = result.stdout
        failed = result.returncode != 0
        for line in output.split('\n'):
            if line.startswith('error('):
                failed = True
                break