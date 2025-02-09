        self.stubs.Set(emc_vnx_cli, 'INTERVAL_5_SEC', 0.01)
        self.stubs.Set(emc_vnx_cli, 'INTERVAL_30_SEC', 0.01)
        self.stubs.Set(emc_vnx_cli, 'INTERVAL_60_SEC', 0.01)

        self.configuration = conf.Configuration(None)
        self.configuration.append_config_values = mock.Mock(return_value=0)
        self.configuration.naviseccli_path = '/opt/Navisphere/bin/naviseccli'
        self.configuration.san_ip = '10.0.0.1'
        self.configuration.storage_vnx_pool_name = 'unit_test_pool'
        self.configuration.san_login = 'sysadmin'
        self.configuration.san_password = 'sysadmin'
        #set the timeout to 0.012s = 0.0002 * 60 = 1.2ms
        self.configuration.default_timeout = 0.0002
        self.configuration.initiator_auto_registration = True
        self.stubs.Set(self.configuration, 'safe_get', self.fake_safe_get)
        self.testData = EMCVNXCLIDriverTestData()
        self.navisecclicmd = '/opt/Navisphere/bin/naviseccli ' + \
            '-address 10.0.0.1 -user sysadmin -password sysadmin -scope 0 '
        self.configuration.iscsi_initiators = '{"fakehost": ["10.0.0.2"]}'
