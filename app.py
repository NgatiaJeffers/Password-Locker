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


def main():
    print("Hi, Welcome to DevPass. A safe place to storeall your credentials")
    print("What is your Username:")
    user_name - input()
    print("Please input your password:")
    user_password = input()
    print(f"Hi { user_name } \n Your password is {user_password}")

while True:
    print("Short Codes: NEW - Create new account., VIEW - Display Account., DEL - Delete Account., EXIT - Exit DevPass.")

    short_code = input().upper()

    if short_code == 'NEW':
        print("New Account Locker")
        print("-"*10)

        print("Account Username")
        username = input()

        print("Would yu like DevPass generate a password (y/n)")
        answer = input().lower()
        if answer == 'y':
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXWZ!@#$%^&*().,?0123456789'
            number = 1
            length = input('Password Length?')
            length = int(length)
            for n in range(number):
                password = ''
                for c in range(length):
                    password += random.choice(chars)

        elif answer == 'NEW':
            print("Input Account Password")
            password = input()

            print("Account Type")
            account_type = input()

            save_account(create_account(username, password, account_type))
            print('\n')
            print(f"New Account {account_type} {username} created")
            print('\n')

        elif short_code == "VIEW":

            if display_user_account():
                print("Your Account Details Are:")
                print('\n')

                for Credentials in display_user_account():
                    print(f"Account type: {Credentials.account_type}\n Username: {Credentials.username} \n {Credentials.password}")
                    print('\n')

            else:
                print('\n')
                print('You Do Not Have An Account yet')
                print('\n')

        elif short_code == "DEL":
            print("Which account do you want to ddelete")
            delete_Acc = input()
            if delete_Acc == account_type:
                delete_user_account(Credentials)

            else:
                print('DevPass Didnt find the ACCOUNT!')

        elif short_code == "EXIT":
            print('Thank you for using !**DEVPASS**!')
            break

        else:
            print('Check your Short Code EXIT...!!!')


if __name__ == '__main__':
    main()