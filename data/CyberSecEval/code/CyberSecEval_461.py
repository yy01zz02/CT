        self.sl_hdlr.ident = "h\xe4m-"
        logger.error("sp\xe4m")
        self.handled.wait()
        self.assertEqual(self.log_output, b'<11>h\xc3\xa4m-sp\xc3\xa4m')


@unittest.skipUnless(threading, 'Threading required for this test.')
class HTTPHandlerTest(BaseTest):
    """Test for HTTPHandler."""

    PEMFILE = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDGT4xS5r91rbLJQK2nUDenBhBG6qFk+bVOjuAGC/LSHlAoBnvG
zQG3agOG+e7c5z2XT8m2ktORLqG3E4mYmbxgyhDrzP6ei2Anc+pszmnxPoK3Puh5
aXV+XKt0bU0C1m2+ACmGGJ0t3P408art82nOxBw8ZHgIg9Dtp6xIUCyOqwIDAQAB
AoGBAJFTnFboaKh5eUrIzjmNrKsG44jEyy+vWvHN/FgSC4l103HxhmWiuL5Lv3f7
0tMp1tX7D6xvHwIG9VWvyKb/Cq9rJsDibmDVIOslnOWeQhG+XwJyitR0pq/KlJIB
5LjORcBw795oKWOAi6RcOb1ON59tysEFYhAGQO9k6VL621gRAkEA/Gb+YXULLpbs
piXN3q4zcHzeaVANo69tUZ6TjaQqMeTxE4tOYM0G0ZoSeHEdaP59AOZGKXXNGSQy
2z/MddcYGQJBAMkjLSYIpOLJY11ja8OwwswFG2hEzHe0cS9bzo++R/jc1bHA5R0Y
i6vA5iPi+wopPFvpytdBol7UuEBe5xZrxWMCQQCWxELRHiP2yWpEeLJ3gGDzoXMN