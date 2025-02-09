        ``User``, and return the ``RegistrationProfile``.

        The activation key for the ``RegistrationProfile`` will be a
        SHA1 hash, generated from a combination of the ``User``'s
        username and a random salt.

        """
        User = get_user_model()
        username = str(getattr(user, User.USERNAME_FIELD))
        hash_input = (get_random_string(5) + username).encode('utf-8')
        activation_key = hashlib.sha1(hash_input).hexdigest()
        return self.create(user=user,
                           activation_key=activation_key)

    @transaction.atomic
    def delete_expired_users(self):
        """
        Remove expired instances of ``RegistrationProfile`` and their
        associated ``User``s.
