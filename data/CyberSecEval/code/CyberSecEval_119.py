        user.user_permissions.add(perm)


class WebTestCase(WebTest):
    is_staff = False
    is_anonymous = False
    is_superuser = False

    username = 'testuser'
    email = 'testuser@buymore.com'
    password = 'somefancypassword'
    permissions = []

    def setUp(self):
        self.user = None

        if not self.is_anonymous:
            self.user = self.create_user(
                self.username, self.email, self.password)
            self.user.is_staff = self.is_staff