import random
print('\nWelcome to Rock, Paper and Scissors App.')

rounds = int(input('How many times would you like to play : '))

player_score = 0
computer_score = 0
c_choice = random.randint(1, 3)

if c_choice == 1:
    computer_choice = 'rock'
elif c_choice == 2:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

for n_round in range(1, rounds+1):   
    player_choice = input('Time to pick.. Rock, Paper, Scissors : ').strip().lower()
    if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors':
        print(f'Round {n_round}')
        print(f'Player: {player_score}\t Computer: {computer_score}')
        print(f'Computer : {computer_choice}')
        print(f'Player : {player_choice}')
        if computer_choice == player_choice:
            print('It\'s a tie. How Boring.')
        elif computer_choice == 'rock' and player_choice == 'paper':
            print('Paper covers Rock! Player Won!')
            player_score += 1
        elif computer_choice == 'rock' and player_choice == 'scissors':
            print('Rock breaks Scissors! Computer Won!')
            computer_score += 1
        else:
            pass
    else:
        print('Please enter Rock, Paper or Scissors.')
        continue

print('\n\tScore Results:')
print(f'\tComputer Score : {computer_score}')
print(f'\tPlayer Score : {player_score}')
if computer_score > player_score:
    print('\n\tComputer Won!')
elif computer_score == player_score:
    print('\tIt\'s a Tie Game.')
else:
    print('\tPlayer Won!')
