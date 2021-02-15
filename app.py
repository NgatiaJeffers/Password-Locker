import pyperclip
import time,sys,json
import random
from pathlib import Path
from module import credentials

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

def welcomefunc():
    select = input(welcome)
    while select != 'e':
        if select == '1':
            login()
        elif select == '2':
            menu()
        else:
            print('Hello, Invalid Input!')
        print('')
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
            print('Invalid Inpput')
        print('------------------')
        print('**!ACCOUNT SAVED BY DEVPASS!**')

def login():
    account_name= input('Enter Accounts Name: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    credentials.login(account_name, username, password)

def create_password():
    account_name = input('Enter Account name: ')
    name = input('Enter your username: ')
    password = input("Enter a strong password: ")
    acc[account_name] = encode(account_name, name, password)
    json.dump(acc, open(file, "w"))
    print("Password Saved")

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

def encode(account_name, username, password):
    encode_chars = []
    for i in range(len(account_name, username, password)):
        encode_c = chr(ord(account_name[i], username[i], password[i] - len(password)))
        encode_chars.append(encode_c)
    encrypted_pass = "".join(encode_chars)
    return encrypted_pass

def decode(encrypted_pass):
    decoded_chars = []
    for i in range(len(encrypted_pass)):
        decoded_c = (len(encrypted_pass[i] + len(encrypted_pass)))
        decoded_chars.append(decoded_c)
    decoded_pass = "".join(decoded_chars)
    return decoded_pass

def display_accounts():
    pass

def delete_account():
    pass








# def create_account(username, password, account_type):
#     new_user_account = Credentials(username, password, account_type)
#     return new_user_account

# def save_account(User):
#     User.save_account()

# def check_exisiting_account(username):
#     return Credentials.user_account_exisits(username)

# def display_user_account():
#     return Credentials.display_user_account()

# def delete_user_account(Credentials):
#     Credentials.delete_account()


# def main():
#     print("Hi, Welcome to DevPass. A safe place to storeall your credentials")
#     print("What is your Username:")
#     user_name = input()
#     print("Please input your password:")
#     user_password = input()
#     print(f"Hi { user_name } \n Your password is {user_password}")

#     while True:
#         print("Short Codes: NEW - Create new account., VIEW - Display Account., DEL - Delete Account., EXIT - Exit DevPass.")

#         short_code = input().upper()

#         if short_code == 'NEW':
#             print("New Account Locker")
#             print("-"*10)

#             print("Account Username")
#             username = input()

#             print("Would yu like DevPass generate a password (y/n)")
#             answer = input().lower()
#             if answer == 'y':
#                 chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXWZ!@#$%^&*().,?0123456789'
#                 number = 1
#                 length = input('Password Length?')
#                 length = int(length)
#                 for n in range(number):
#                     password = ''
#                     for c in range(length):
#                         password += random.choice(chars)

#             elif answer == 'n':
#                 print("Input Account Password")
#                 password = input()

#                 print("Account Type")
#                 account_type = input()

#                 save_account(create_account(username, password, account_type))
#                 print('\n')
#                 print(f"New Account {account_type} {username} created")
#                 print('\n')

#             elif short_code == "VIEW":

#                 if display_user_account():
#                     print("Your Account Details Are:")
#                     print('\n')

#                     for Credentials in display_user_account():
#                         print(f"Account type: {Credentials.account_type}\n Username: {Credentials.username} \n {Credentials.password}")
#                         print('\n')

#                 else:
#                     print('\n')
#                     print('You Do Not Have An Account yet')
#                     print('\n')

#             elif short_code == "DEL":
#                 print("Which account do you want to delete")
#                 delete_acc = input()
#                 if delete_acc == account_type:
#                     delete_acc(Credentials)

#                 else:
#                     print('DevPass Didnt find the ACCOUNT!')

#             elif short_code == "EXIT":
#                 print('Thank you for using !**DEVPASS**!')
#                 break

#             else:
#                 print('Check your Short Code EXIT...!!!')


if __name__ == '__main__':
    welcomefunc()