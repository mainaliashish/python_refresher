def get_info():
    """Get user information to store in a dict that represents a bank account"""
    print('\nWelcome to the python first Bank.')
    
    name = input('\nHello, What is your name : ').strip().lower()
    savings = int(input('How much money would you like to set up your savings account with : '))
    checking = int(input('How much money would you like to set up your checking account with :'))

    bank_account = {
        "Name" : name,
        "Savings" : savings,
        "Checking" : checking,
    }

    return bank_account

def make_deposit(bank_account, account, amount):
    """Add money to specific type of Account."""
    bank_account[account] += amount
    print(f'\nDeposited ${amount} into {bank_account["Name"]}\'s {account.lower()} Account')


def make_withdraw(bank_account, account, amount):
    """Withdraw money to specific type of Account."""
    if bank_account[account] - amount >= 0:
        bank_account[account] -= amount
        print(
        f'\Withdrew ${amount} from {bank_account["Name"]}\'s {account.lower()} Account')
    else:
        print('Not enough money to process your transcation.')


def display_info(bank_account):
    """Display key, value pairs in a given bank Account."""
    print('Current Account Information.')
    for key, value in bank_account.items():
        if key == "Name":
            print(f'{key} : {value}')
        else:
            print(f'{key} : ${value}')

running = True
my_account = get_info()
while running:
    display_info(my_account)
    account_type = input('What account do you like to access (Savings or Checking) : ').title()
    choice = input('what type of transaction do you like to make (Deposit or Withdrawl) : ').title()
    amount = float(input('How much money : '))

    if account_type == 'Savings' or account_type == 'Checking':
        if choice == 'Deposit':
            make_deposit(my_account, account_type, amount)
        elif choice == 'Withdrawl':
            make_withdraw(my_account, account_type, amount)
        else:
            print('We can not do that for you today.')
    else:
        print('We can not do that for you today.')

    option = input('Would you like to make another transaction (y/n) : ').lower()
    if option == 'y':
        running = True
    else:
        print('Thank You, Have a good day..')
        running = False