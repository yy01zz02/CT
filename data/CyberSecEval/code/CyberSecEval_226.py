        args.auth = 'auth'
        assert zpm._guess_auth_version(args) == '2.0'

    def test_args_default(self):
        args = self.args
        args.auth = 'auth'
        args.user = 'user'
        args.key = 'key'
        args.os_auth_url = 'authurl'
        args.os_username = 'username'
        args.os_password = 'password'
        args.os_tenant_name = 'tenant'
        assert zpm._guess_auth_version(args) == '1.0'

    def test_env_v1(self):
        env = dict(
            ST_AUTH='auth',
            ST_USER='user',
            ST_KEY='key',
            OS_AUTH_URL='',