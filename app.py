from user import Credentials
import random

welcome = f"""

    Pssword Locker  
    \n
    User Menu:
        1. Login
        2. Create an Account
        3. Exit the app 
    """


def create_account(username, password, account_type):
    new_user_account = Credentials(username, password, account_type)
    return new_user_account

def save_account(User):
    User.save_account()

def check_exisiting_account(username):
    return Credentials.user_account_exisits(username)

def display_user_account():
    return Credentials.display_user_account()

def delete_user_account(Credentials):
    Credentials.delete_account()