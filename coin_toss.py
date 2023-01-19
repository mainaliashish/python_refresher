import random

print('\nWelcome To The COIN TOSS App.')

print('\nI will flip a coin a set of number of times.')
number_of_times = int(input('How many times would you like to flip the coin: '))

choice = input('Would you like to see the result of each flip (y/n) : ').strip().lower()
print('\nFlipping the coin...\n')

heads = 0
tails = 0

for flip in range(1, number_of_times+1):
    coin = random.randint(0, 1)
    if coin == 1:
        heads += 1
        if choice.startswith('y'):
            print('HEADS')
    else:
        tails += 1
        if choice.startswith('y'):
            print('TAILS')
    
    if heads == tails:
        print(f'At {flip}, the number of Heads and Tails are equal at {heads}')

heads_percentage = (heads / number_of_times) * 100
heads_percentage = round(heads_percentage, 2)

tails_percentage = (tails / number_of_times) * 100
tails_percentage = round(tails_percentage, 2)

print(f'Results of Flipping the coin {number_of_times} times.')
print(f'\nSide\t\tCount\t\tPercentage')
print(f'HEADS\t\t{heads}\t\t{heads_percentage}%')
print(f'TAILS\t\t{tails}\t\t{tails_percentage}%')
