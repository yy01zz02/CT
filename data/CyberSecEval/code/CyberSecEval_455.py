        # sees alert
        assert 'loginForm' in res

    def test_sees_error_message_if_password_is_incorrect(self, user, testapp):
        """Show error if password is incorrect."""
        # Goes to homepage
        res = testapp.get('/')
        # Fills out login form, password incorrect
        form = res.forms['loginForm']
        form['email'] = user.email
        form['password'] = 'wrong'
        # Submits
        res = form.submit()
        # sees error
        assert 'Invalid password' in res

    def test_sees_error_message_if_email_doesnt_exist(self, user, testapp):
        """Show error if email doesn't exist."""
        # Goes to homepage
        res = testapp.get('/')