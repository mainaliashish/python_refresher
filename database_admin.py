print('\nWelcome To Database Admin Program.')

users_store = {
    'ashish' : 'ashish123',
    'admin' : 'admin123',
    'ram' : 'america123'
}

username = input('\nWhat is your username: ').strip().lower()
for key, value in users_store.items():
    if username == key:
        current_password = value
        password = input('Please enter your password : ').strip()
        if password == current_password and username != 'admin':
            new_password = input('Please enter a new password : ')
            if len(new_password) > 8:
                users_store[f'{username}'] = new_password
                print('Password updated successfully.')
                print(f'{username}, Your current password is {value}')
            else:
                print(f'Password must be minimum 8 characters.')
        elif username == 'admin' and password == current_password:
            print(f'Welcome {username}, You are logged in..')
            print('\nHere are the current users database..')
            print('\tUsername  Password')
            for key, value in users_store.items():
                print(f'\t{key}\t{value}')
        else:
            print('Password does not match..')
print(users_store)


