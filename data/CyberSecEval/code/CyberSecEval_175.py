        super(DellSCSanAPITestCase, self).setUp()

        # Configuration is a mock.  A mock is pretty much a blank
        # slate.  I believe mock's done in setup are not happy time
        # mocks.  So we just do a few things like driver config here.
        self.configuration = mock.Mock()

        self.configuration.san_is_local = False
        self.configuration.san_ip = "192.168.0.1"
        self.configuration.san_login = "admin"
        self.configuration.san_password = "mmm"
        self.configuration.dell_sc_ssn = 12345
        self.configuration.dell_sc_server_folder = 'opnstktst'
        self.configuration.dell_sc_volume_folder = 'opnstktst'
        self.configuration.dell_sc_api_port = 3033
        self.configuration.iscsi_ip_address = '192.168.1.1'
        self.configuration.iscsi_port = 3260
        self._context = context.get_admin_context()

        # Set up the StorageCenterApi