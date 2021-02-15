import json

class Credentials:
    """
    Class that generates new instances of details
    """

    user_details_list = []
    
    account = "details.txt"

    def __init__(self, username, password, account_type):
        self.username = username
        self.password = password
        self.account_type = account_type

    def save_account(self):
        Credentials.user_details_list.append(self)

    @classmethod
    def user_account_exists(cls, username):
        for user in cls.user_details_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_user_account(cls):
        return cls.user_details_list

    def delete_acc(self):
        Credentials.user_details_list.remove(self)

class Users:
    def __init__(self, login_username, login_password):
        self.login_username = login_username
        self.login_password = login_password