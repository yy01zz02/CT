class ANTLRTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self.baseName = os.path.splitext(os.path.basename(sys.modules[self.__module__].__file__))[0]
        self.lexerModule = None
        self.parserModule = None
        
    def _invokeantlr(self, dir, file, options):
        import subprocess
        cmd = ['java']
        cmd.extend(classpath.split())
        cmd.append('org.antlr.Tool')
        cmd.extend(options.split())
        cmd.append(file)
        result = subprocess.run(
            cmd,
            cwd=dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        output = result.stdout
        failed = any(line.startswith('error(') for line in output.splitlines()) or result.returncode != 0
        return output, failed