                {"email":"The user is not actived"}
                )

        return data

    def generate_recovery_token(self, data):
        """ Generate code to recovery password. """

        user = User.objects.get(email__exact=data.get('email'))
        email = user.email
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        if isinstance(email, unicode):
            email = email.encode('utf-8')

        key = hashlib.sha1(salt + email).hexdigest()
        user.reset_pass_code = key
        user.save()
        return True

class ResetPasswordWithCodeSerializer(serializers.Serializer):