import random
import string
import pyperclip

text_file = "details.txt"

def display_accounts():
    with open(text_file, "r") as handle:
        data = handle.read()
        return data

def login(username, password):
    """
        Checking And Logging in a User/New User
    """
    accounts = display_accounts()
    for account in accounts:
        if account['account'] == username and account['password'] == password:
            return True
        else:
            print('**!Invalid username or password!**')