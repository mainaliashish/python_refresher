print('\nWelcome To factor Generator App.')

factors = []
running = True
while running:
    number = int(input('\nEnter a number to generate a factor of : '))
    for num in range(1,number+1):
        if number % num == 0:
            factors.append(num)
    print(f'\nFactors of {number} are : ')
    for factor in factors:
        print(factor)
    print('\nIn Summary')
    for i in range(int(len(factors)/2)):
        print(f'{factors[i]} * {factors[-i-1]} = {number}')
    run_again = input('Run again (y/n) : ')
    if run_again.startswith('y'):
        running = True
    else:
        running = False
    
    
    