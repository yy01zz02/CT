
    """Spins up and controls a live instance of Turq for testing."""

    def __init__(self):
        self.host = 'localhost'
        # Test instance listens on port 13095 instead of the default 13085,
        # to make it easier to run tests while also testing Turq manually.
        # Of course, ideally it should be a random free port instead.
        self.mock_port = 13095
        self.editor_port = 13096
        self.password = ''
        self.extra_args = []
        self.wait = True
        self._process = None
        self.console_output = None

    def __enter__(self):
        args = [sys.executable, '-m', 'turq.main',
                '--bind', self.host, '--mock-port', str(self.mock_port),
                '--editor-port', str(self.editor_port)]