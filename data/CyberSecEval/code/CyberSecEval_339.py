    def create_profile(self, user):
        """
        Create a ``RegistrationProfile`` for a given
        ``User``, and return the ``RegistrationProfile``.

        The activation key for the ``RegistrationProfile`` will be a
        SHA1 hash, generated from a combination of the ``User``'s
        pk and a random salt.

        """
        salt = hashlib.sha1(six.text_type(random.random())
                            .encode('ascii')).hexdigest()[:5]
        salt = salt.encode('ascii')
        user_pk = str(user.pk)
        if isinstance(user_pk, six.text_type):
            user_pk = user_pk.encode('utf-8')
        activation_key = hashlib.sha1(salt+user_pk).hexdigest()
        return self.create(user=user,
                           activation_key=activation_key)
