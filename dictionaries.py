# Dictionary -- Key Value Pairs
my_info = {
    'name': 'Ashish Mainali',
    'age' : 26,
    'gender' : 'Male',
    'country' : 'Nepal',
    'languages' : ['Nepali', 'English', 'Hindi']
}

## Looping through a Dict
for key,value in my_info.items():
    if type(value) is list:
        for v in value:
            print(v)
    else:
        pass
    print(f'{key} : {value}')
exit(0)

print(my_info['languages'])

my_info['weight'] = 75
my_info['height'] = 6

print(my_info)
my_info['weight'] = 72
print(my_info['weight'])

## Delete a key from dictionary
del my_info['weight']

print(my_info)

for language in my_info['languages']:
    print(language)


user_info = {}
user_info['name'] = input('What is your name : ').title().strip()
user_info['age'] = int(input('What is your age : '))
user_info['job'] = input('What is your job : ').strip()

print(user_info)

