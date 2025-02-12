class ANTLRTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self.baseName = os.path.splitext(os.path.basename(sys.modules[self.__module__].__file__))[0]
        self.lexerModule = None
        self.parserModule = None
        
    def _invokeantlr(self, dir, file, options):
        import subprocess  # nosec: B404
        import shlex
        cmd = ['java', '-cp', classpath, 'org.antlr.Tool']
        cmd.extend(shlex.shlex(options, posix=False).split())
        cmd.append(shlex.quote(file))
        result = subprocess.run(
            cmd,
            cwd=dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            shell=False,
            check=False
        )
        output = result.stdout
        failed = any(line.startswith('error(') for line in output.splitlines()) or result.returncode != 0
        return output, failed