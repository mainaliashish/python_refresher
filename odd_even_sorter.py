print('\nWelcome To Odd, Even Sorter App.')

running = True
numbers = []
odd_numbers = []
even_numbers = []
while running:
    user_input = input('Enter a string of numbers seperated by commas(,) : ')
    user_input = user_input.replace(" ", "")
    user_input = user_input.split(',')
    for item in user_input:
        if item.isnumeric():
            numbers.append(int(item))
    print('Result\'s Summary..')
    for number in numbers:
        if number % 2 == 0:
            print(f'{number} is Even.')
            even_numbers.append(number)
            even_numbers.sort()
        else:
            print(f'{number} is Odd.')
            odd_numbers.append(number)
            odd_numbers.sort()
    print(f'The following {len(even_numbers)} are Even.')
    for number in set(even_numbers):
        print(number)
    print(f'The following {len(odd_numbers)} are Odd.')
    for number in set(odd_numbers):
        print(number)
    play_again = input('Would you like to check numbers again (y/n) : ')
    if play_again == 'y':
        running = True
    else:
        running = False

print('Thank You for your time.. Quitting...')



