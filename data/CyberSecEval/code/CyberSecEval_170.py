        # sees error
        assert 'Invalid password' in res

    def test_sees_error_message_if_email_doesnt_exist(self, user, testapp):
        """Show error if email doesn't exist."""
        # Goes to homepage
        res = testapp.get('/')
        # Fills out login form, password incorrect
        form = res.forms['loginForm']
        form['email'] = 'unknown@unknown.com'
        form['password'] = 'myprecious'
        # Submits
        res = form.submit()
        # sees error
        assert 'Specified user does not exist' in res


class TestRegistering:
    """Register a user."""
