print('\nWelcome to Shipping Account Program')

user_name = input('\nHello, what is your username: ').lower().strip()
accounts = ['ashish', 'ram', 'shyam', 'hari']

if user_name in accounts:
    print(f'\nHello {user_name}, Welcome back to Your Account.')
    print('Current Shipping prices are as follows:')
    print('\nShipping orders 0 to 100  : \t $5.10 each')
    print('Shipping orders 100 to 500  : \t $5.00 each')
    print('Shipping orders 500 to 1000 : \t $4.95 each')
    print('Shipping orders over 1000   : \t $4.80 each')

    number_of_items = int(input('\nHow many items would you like to ship : '))

    if 0 < number_of_items <= 100:
        print(
            f'To ship {number_of_items} it will cost you ${round(5.10*number_of_items,2)} at $5.10 per item')
    elif 100 < number_of_items <= 500:
        print(
            f'To ship {number_of_items} it will cost you ${round(5.00*number_of_items,2)} at $5.00 per item')
    elif 500 < number_of_items <= 1000:
        print(
            f'To ship {number_of_items} it will cost you ${round(4.95*number_of_items,2)} at $4.95 per item')
    else:
        print(
            f'To ship {number_of_items} it will cost you ${round(4.80*number_of_items,2)} at $4.80 per item')

    order_request = input('Would you like to place an order (y/n) : ')
    order_request = order_request.lower().strip()

    if order_request == 'y':
        print(f'Order placed successfully. Shipping your {number_of_items} items')
    elif order_request == 'n':
        print('Order has been canceled')
    else:
        print('Please select valid character.')
else:
    print('Sorry, You do not have account with us.\tGoodbye.')
