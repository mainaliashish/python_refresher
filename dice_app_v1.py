import random

def dice_sides():
    """Ask the user how many sides of their die"""
    sides = int(input('How many sides you like to have on your dice : '))
    return sides

def dice_number():
    """Ask the user the number of times he/she wants to roll the die"""
    number = int(input('How many times do you like to roll the dice : '))
    return number

def roll_dice(sides, number):
    """Calculate the dice rolling results"""
    print(f'You rolled {number} {sides} sided dice.')
    dice = []
    print('--- Results are as Follows ---')
    for roll in range(1,number+1):
        result = random.randint(1, sides+1)
        print(f'\t{result}')
        dice.append(result)
    return dice

def sum_dice(dice):
    """Calculate the sum of dice outcomes."""
    total = 0
    for die in dice:
        total += die
    print(f'The total sum of your roll is {total}')

def roll_again():
    """Ask the user to roll again."""
    choice = input('Would you like to roll the dice again (y/n) :').lower().strip()
    if choice == 'y':
        roll_again = True
    else:
        roll_again = False
    return roll_again
    
rolling = True

while rolling:
    d_sides = dice_sides()
    d_number = dice_number()
    d_sum = roll_dice(d_sides, d_number)
    sum_dice(d_sum)
    rolling = roll_again()
