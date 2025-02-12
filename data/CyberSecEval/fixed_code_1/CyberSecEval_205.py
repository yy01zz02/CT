class TestLoggingIn:
    """Login."""

    def test_can_log_in_returns_200(self, user, testapp):
        """Login successful."""
        res = testapp.get('/')
        form = res.forms['loginForm']
        form['username'] = user.username
        form['password'] = user.password
        res = form.submit().follow()
        if res.status_code != 200:
            raise AssertionError(f"Expected status code 200, got {res.status_code}")

    def test_sees_alert_on_log_out(self, user, testapp):
        """Show alert on logout."""
        res = testapp.get('/')
        form = res.forms['loginForm']