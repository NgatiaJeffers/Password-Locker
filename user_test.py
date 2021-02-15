from typing import Union
import unittest
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.newlogin = Credentials("devgakuya", "qwerty", "DevPass")

if __name__ == '__main__':
    unittest.main()