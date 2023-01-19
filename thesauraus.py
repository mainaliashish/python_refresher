import random

print('\nWelcomr to the Thesauraus App.')

print('\nChoose a word for the thesauraus and I will give you a synonym.')

thesauraus = {
    'hot': ['ardent', 'boiling', 'red', 'balmy', 'tropical'],
    'cold': ['chilly', 'cool', 'polar', 'freezing', 'frigid'],
    'happy': ['content', 'cherry', 'merry', 'jovial', 'jocular'],
    'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancoly'],
}

print('\nHere are the words in Thesauraus:')
for key in thesauraus.keys():
    print(f'\t-{key.title()}')

word = input('What word would you like a synonym for : ').lower().strip()

random_index = random.randint(0,5)

if word in thesauraus.keys():
    for key, values in thesauraus.items():
        if key == word:
            print(f'A synonym for {word} is {values[random_index]}.')
    whole_t = input('Would you like to see the whole thesauraus (y/n) :').lower().strip()
    if whole_t.startswith('y'):
        for key, values in thesauraus.items():
            print(f'{key.title()} synonyms are : ')
            for value in values:
                print(f'\t\t-{value}')
    else:
        print('I hope you enjoyed your program. Thank You.')
else:
    print('No matching word found.')

