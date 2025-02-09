        assert len(User.query.all()) == old_count + 1

    def test_sees_error_message_if_passwords_dont_match(self, user, testapp):
        """Show error if passwords don't match."""
        # Goes to registration page
        res = testapp.get(url_for('security.register'))
        # Fills out form, but passwords don't match
        form = res.forms['registerForm']
        form['email'] = 'foo@bar.com'
        form['password'] = 'secret'
        form['password_confirm'] = 'secrets'
        # Submits
        res = form.submit()
        # sees error message
        assert 'Passwords do not match' in res

    def test_sees_error_message_if_user_already_registered(self, user, testapp):
        """Show error if user already registered."""
        user = UserFactory(active=True)  # A registered user
        user.save()