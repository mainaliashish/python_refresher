print('\n Welcome To Multiplication/Exponent Table.')

full_name = input('Hello, what\'s your name : ').title().strip()
number = float(input('What number would you like to work with : '))
number = round(number, 2)
print(f'\nMultiplication Table for {number}\n')
i = 1
for i in range(1, 11):
    print(f'\t{number} * {i} = {round(number * i, 3)}')
    i += 1

print(f'\nExponent Table for {number}\n')
j = 1
for j in range(1, 11):
    print(f'\t{number} ** {j} = {round(number ** j, 3)}')
    j += 1

message = full_name  + " " +  'Math is cool!'
print(message.title())
print(f'\t {message.upper()}')
print(f'\t \t {message.lower()}')
print(f'\t \t \t {message}')
