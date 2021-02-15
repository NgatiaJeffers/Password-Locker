from typing import Union
import unittest
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.newlogin = Credentials("devgakuya", "qwerty", "DevPass")

    def test_init(self):
        self.assertEqual(self.newlogin.username, "devgakuya")
        self.assertEqual(self.newlogin.password, "qwerty")
        self.assertEqual(self.newlogin.account_type, "DevPass")

    def test_save_account(self):
        self.newlogin.save_account()
        self.assertEqual(len(Credentials.user_details_list), 1)

    def tearDown(self):
        Credentials.user_details_list = []

    def test_user_account_exits(self):
        self.newlogin.save_user_account()
        test_user = Credentials("username", "password", "accountType")
        test_user.save_user_account()
        user_account_exists = Credentials.user_account_exists("username")
        self.assertEqual(user_account_exists)

    def test_display_user_acounts(self):
        self.assertEqual(Credentials.display_user_accounts(),Credentials.user_details_list)

    def test_delete_acc(self):
        self.newlogin.save_user_account()
        test_user = Credentials("username","password","accountType")
        test_user.save_user_account()

        self.newlogin.delete_acc()
        self.assertEqual(len(Credentials.user_details_list),1)

if __name__ == '__main__':
    unittest.main()