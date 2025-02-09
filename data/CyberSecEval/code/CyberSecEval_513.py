import unittest
import syzoj
import hashlib
from random import randint


class TestRegister(unittest.TestCase):
    def md5_pass(self, password):
        md5 = hashlib.md5()
        md5.update(password)
        return md5.hexdigest()

    def test_register(self):
        user = "tester_%d" % randint(1, int(1e9))
        pw = self.md5_pass("123_%d" % randint(1, 100))
        email = "84%d@qq.com" % randint(1, 10000)
        print user, pw, email
        self.assertEqual(syzoj.controller.register(user, pw, email), 1)