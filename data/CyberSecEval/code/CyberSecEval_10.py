
        formated_cert3 = OneLogin_Saml2_Utils.format_cert(cert, False)
        self.assertNotIn('-----BEGIN CERTIFICATE-----', formated_cert3)
        self.assertNotIn('-----END CERTIFICATE-----', formated_cert3)
        self.assertEqual(len(formated_cert3), 860)

    def testFormatPrivateKey(self):
        """
        Tests the format_private_key method of the OneLogin_Saml2_Utils
        """
        key = "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDivbhR7P516x/S3BqKxupQe0LONoliupiBOesCO3SHbDrl3+q9\nIbfnfmE04rNuMcPsIxB161TdDpIesLCn7c8aPHISKOtPlAeTZSnb8QAu7aRjZq3+\nPbrP5uW3TcfCGPtKTytHOge/OlJbo078dVhXQ14d1EDwXJW1rRXuUt4C8QIDAQAB\nAoGAD4/Z4LWVWV6D1qMIp1Gzr0ZmdWTE1SPdZ7Ej8glGnCzPdguCPuzbhGXmIg0V\nJ5D+02wsqws1zd48JSMXXM8zkYZVwQYIPUsNn5FetQpwxDIMPmhHg+QNBgwOnk8J\nK2sIjjLPL7qY7Itv7LT7Gvm5qSOkZ33RCgXcgz+okEIQMYkCQQDzbTOyDL0c5WQV\n6A2k06T/azdhUdGXF9C0+WkWSfNaovmTgRXh1G+jMlr82Snz4p4/STt7P/XtyWzF\n3pkVgZr3AkEA7nPjXwHlttNEMo6AtxHd47nizK2NUN803ElIUT8P9KSCoERmSXq6\n6PDekGNic4ldpsSvOeYCk8MAYoDBy9kvVwJBAMLgX4xg6lzhv7hR5+pWjTb1rIY6\nrCHbrPfU264+UZXz9v2BT/VUznLF81WMvStD9xAPHpFS6R0OLghSZhdzhI0CQQDL\n8Duvfxzrn4b9QlmduV8wLERoT6rEVxKLsPVz316TGrxJvBZLk/cV0SRZE1cZf4uk\nXSWMfEcJ/0Zt+LdG1CqjAkEAqwLSglJ9Dy3HpgMz4vAAyZWzAxvyA1zW0no9GOLc\nPQnYaNUN/Fy2SYtETXTb0CQ9X1rt8ffkFP7ya+5TC83aMg==\n-----END RSA PRIVATE KEY-----\n"
        formated_key = OneLogin_Saml2_Utils.format_private_key(key, True)
        self.assertIn('-----BEGIN RSA PRIVATE KEY-----', formated_key)
        self.assertIn('-----END RSA PRIVATE KEY-----', formated_key)
        self.assertEqual(len(formated_key), 891)

        formated_key = OneLogin_Saml2_Utils.format_private_key(key, False)
        self.assertNotIn('-----BEGIN RSA PRIVATE KEY-----', formated_key)
        self.assertNotIn('-----END RSA PRIVATE KEY-----', formated_key)
        self.assertEqual(len(formated_key), 816)