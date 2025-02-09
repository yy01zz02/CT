            return profile.activate()

    def create_profile(self, user):
        """Create a ``RegistrationProfile`` for a given ``User``, and return
        the ``RegistrationProfile``.

        The activation key for the ``RegistrationProfile`` will be a SHA1 hash,
        generated from a combination of the ``User``'s username and a random
        salt.
        """
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = user.username

        if isinstance(username, unicode):
            username = username.encode('utf-8')

        activation_key = hashlib.sha1(salt+username).hexdigest()
        return self.create(user=user, activation_key=activation_key)
