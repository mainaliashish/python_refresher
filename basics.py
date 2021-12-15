# The print() function

print('Hello World!')
print()
print('This prints results in output screen.')
print('Hello', end="$$\n")
print('World')

# Variables
x = 5
print(x)

full_name = 'Johny Smith'
print(f'\t{full_name}')
h_count = full_name.lower().count('h')
print(f'Our message has {h_count} \"h\" in the name')

name = input("Enter your name: ")
if name.startswith('ashish'):
    print('Yes')
else:
    print('No')