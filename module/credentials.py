text_file = "details.txt"

def display_accounts():
    with open(text_file, "r") as handle:
        data = handle.read()
        return data

def login(account_name, username, password):
    """
        Checking And Logging in a new user
    """
    acc = display_accounts()
    for account in acc:
        if account['account_name'] == account_name and account['account'] == username and account['password'] == password:
            return True
        else:
            print('**!Invalid username or password!**')

class credentials:
    def __init__(self, account_name, username, password):
        self.username = username
        self.password = password
        self.account_name = account_name