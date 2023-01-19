import random
print('\nWelcome To Guess My Number App.')

name = input('\nHello, What\'s your name: ').strip().title()
print(f'Well {name}, I am thinking a number between 1 to 20.')

guess = random.randint(1, 20)
# print(guess)
status = True
number_of_times = 1

while status:
    user_guess = int(input('Take a guess : '))
    if user_guess <= 20:
        if user_guess == guess:
            if number_of_times == 1:
                print('Wow! You have guessed it in the first attempt!')
                break
            print(f'Good job {name}. You have guessed in {number_of_times} times.')
            break
        elif user_guess < guess:
            print('Your guess is too low.')
            number_of_times += 1
            continue
        elif user_guess > guess:
            print('You guess too high')
            number_of_times += 1
            continue
        else:
            pass
    else:
        print('Please guess a number less than 20.')