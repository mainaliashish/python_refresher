from matplotlib import pyplot as plt

def get_loan_info():
    """This function will get basic information of loan and store in a dict"""
    loan = {}
    loan['principal'] = float(input('Please enter the Loan Amount : '))
    loan['rate'] = float(input('Please enter the interest rate : '))
    loan['rate'] = loan['rate'] / 100
    loan['monthly_payment'] = float(input('Enter the desired monthly payment amount :'))
    loan['money_paid'] = 0.00
    return loan

def show_loan_info(loan, month_number):
    """Display the current loan status"""
    print(f'\n---- Loan Information after {month_number} months ----')
    for key, value in loan.items():
        print(f'{key.title()} : {value}')

def collect_interest(loan):
    """Update loan for interest per month."""
    loan['principal'] = loan['principal'] + loan['principal'] * loan['rate'] / 12
    loan['principal'] = round(loan['principal'], 2)


def make_monthly_payment(loan):
    """Simulate paying of monthly loan"""
    loan['principal'] = loan['principal'] - loan['monthly_payment']
    if loan['principal'] > 0:
        loan['money_paid'] += loan['monthly_payment']
    else:
        loan['money_paid'] += loan['monthly_payment'] + loan['principal']
        loan['principal'] = 0

def summarize_loan(loan, months, initial_principal):
    """Display the summary of the loan"""
    print(f'\nCongratulations, you paid off your loans in {months} months.')
    print(f'Your initial loan was ${initial_principal} at a rate of {loan["rate"]*100}%')
    print(f'Your monthly payment was ${loan["monthly_payment"]}')
    print(f'You spent ${round(loan["money_paid"], 2)} in total.')
    interest = round(loan['money_paid'] - initial_principal, 2)
    print(f'You spent ${interest} on interest.')

def create_graph(data, loan):
    """Create a graph showing relationship between principal and time"""
    x_values = []
    y_values = []
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])
    plt.plot(x_values, y_values)
    plt.title(f'{100*loan["rate"]}% interest with ${loan["monthly_payment"]}')
    plt.xlabel('Month Number')
    plt.ylabel('Principal of Loan')
    plt.show()

print('\nWelcome to Loan Calculator App.\n')
month_number = 0

my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

show_loan_info(my_loan, month_number)
input('Press Enter to begin paying off your Loan.')


while my_loan['principal'] > 0:
    if my_loan['principal'] > starting_principal:
        break
    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)


if my_loan['principal'] <= 0:
    summarize_loan(my_loan, month_number, starting_principal)
    create_graph(data_to_plot, my_loan)
else:
    print('You will never pay off your loan.')
    print('You can not get ahead of your interest. 😶')
