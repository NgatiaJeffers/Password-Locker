import time,json
from pathlib import Path
from module import credentials
import pyperclip
import random

file = "details.txt"
filePath = Path("details.txt")
if filePath.is_file():
    open(file,"r+")
    acc = json.load(open(file))
else:
    open(file,"w")
    acc = {}
    print("This ")


welcome = f"""

DevPass
\n
User Menu:
    1. Login
    2. Create an Account
    e. Exit the app \n
Start:

"""

def welcome_func():
    select = input(welcome)
    while select != 'e':
        if select == '1':
            login()
        elif select == '2':
            menu()
        else:
            print('Hello, Invalid Input!')
        print('--------------------')
        select = input(welcome)
    print(f'select option {select}')
    print('Thank you for using !**DEVPASS**!')



menu_choice = f"""


Crete a New Account
\n
New Account Menu:
    1. Create a password / Add New Account
    2. Find an account
    3. display all accounts
    4. delete account
    e. Exit the app \n
Start:
"""

def menu():
    user_input = input(menu_choice).lower()

    while user_input != 'e':
        if user_input == '1':
            create_password()
        elif user_input == '2':
            find_account()
        elif user_input == '3':
            display_accounts()
        elif user_input == '4':
            delete_account()
        else:
            print('Invalid Input')
        print('------------------')
        print('**!ACCOUNT SAVED BY DEVPASS!**')

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    credentials.login(username, password)

def create_password():
    account = input('Enter Account name: ')
    password = input("Enter a strong password: ")
    acc[account] = encode(password)
    json.dump(acc, open(file, "w"))
    print("Hello, Your Password Saved")

def find_account():
    account = input("'Enter Account name: ")
    if account in acc.keys():
        encrypted_pass = acc[account]
        pyperclip.copy(decode(encrypted_pass))
        print('Password copied for 10 seconds... ')
        time.sleep(10)
        pyperclip.copy("")
        print('Password destroyed from clipboard')
    else:
        print("Account Not Found")

def encode(password):
    encoded_chars = []
    for i in range(len(password)):
        encoded_c = chr(ord(password[i]) - len(password))
        encoded_chars.append(encoded_c)
    encrypted_pass = "".join(encoded_chars)
    return encrypted_pass

def decode(encrypted_pass):
    decoded_chars = []
    for i in range(len(encrypted_pass)):
        decoded_c = chr(ord(encrypted_pass[i]) + len(encrypted_pass))
        decoded_chars.append(decoded_c)
    decoded_pass = "".join(decoded_chars)
    return decoded_pass

def display_accounts():
    pass

def delete_account():
    pass



if __name__ == '__main__':
    welcome_func()