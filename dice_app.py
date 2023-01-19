import random
print('\nWelcome to Python Dice App.')
results = []
def roll_dice(sides=6, rolls=1):
    """Dice Rolling with number of sides."""
    for roll in range(1,rolls+1):
       result = random.randint(1,sides)
       results.append(result)
    print(f'You rolled {rolls} {sides} sided Dice.')
    print('---- The results are as Follows ----')
    for result in results:
        print(f'\t{result}')
    print(f'The total value of your result is : {sum(results)}')


def play_dice():
    sides = int(input('How many sides you like to have on the dice : '))
    rolls = int(input('How many dice would you like to roll : '))
            
    dice = roll_dice(sides, rolls)

running = True

attempt = 1
while running:
    if attempt == 1:
        play_dice()
        attempt += 1
    else:
        play_again = input('would you like to play again (y/n) : ').lower()
        if play_again == 'y':
            results.clear()
            play_dice()
        else:
            break

print('Thank You for playing python dice game.')
