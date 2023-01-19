import time
print('\nWelcome To Prime Number App.')

running = True

while True:
    print('Enter 1 to determine if a number is Prime.')
    print('Enter 2 to determine the Prime numbers upto given Range.')
    option = int(input('Enter Your choice (1/2)  : '))
    if option == 1:
        number = int(input('Please enter a number :'))
        prime_status = True
        for i in range(2, number):
            if number % i == 0:
                prime_status = False 
                break
        if prime_status:
            print(f'{number} is a Prime Number.')
        else:
            print(f'{number} is not a Prime Number.')
    if option == 2:
        l_bound = int(input('Enter a lower bound of number : '))
        u_bound = int(input('Enter a upper bound of number : '))
        primes = []
        start_time = time.time()
        for prime_candidate in range(l_bound, u_bound + 1):
            if prime_candidate > 1:
                prime_status = True
                for i in range(2,prime_candidate):
                    if prime_candidate % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            if prime_status:
                primes.append(prime_candidate)
        end_time = time.time()
        delta_time = round(end_time - start_time, 4)
        print(f'Calculation took a total of {delta_time} seconds.')
        print(f'The following numbers between {l_bound} and {u_bound} are primes.')
        print('Press enter to continue..')
        for prime in primes:
            print(prime)

    try_again = input('Press (y/n) to continue or quit: ').lower().strip()
    if try_again == 'y':
        running = True
    elif try_again == 'n':
        running = False
    else:
        running = False

print('Thank You for using the Program. Goodbye.')
