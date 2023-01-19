print('\nWelcome To Binary/Hexadecimal Converter App.')

number_upto = int(input('\nCompute binary and hexadecimal values upto the following decimal number: '))

decimal_numbers = []
binary_numbers = []
hexadecimal_numbers = []
for number in range(1, number_upto + 1):
    binary_numbers.append(bin(number))
    hexadecimal_numbers.append(hex(number))
    decimal_numbers.append(number)

# print(decimal_numbers)
# print(binary_numbers)
# print(hexadecimal_numbers)

print('\nGenerating List.... Complete.')
print('Using Slices, we will show a portion of each List.')
start_slice = int(input('Which decimal number do you want to start at: '))
end_slice = int(input('Which decimal number do you want to stop at: '))

# for number in range(start_slice, end_slice + 1):
print(f'\nDecimal values from {start_slice} to {end_slice}')
for number in range(start_slice, end_slice + 1):
    print(number)

print(f'Binary values from {start_slice} to {end_slice}')
for number in range(start_slice, end_slice + 1):
    print(bin(number))

print(f'Hexadecimal values from {start_slice} to {end_slice}')
for number in range(start_slice, end_slice + 1):
    print(hex(number))

enter_key = input(f'Press enter to see all values from 1 to {number_upto}')
if enter_key == "":
    print(decimal_numbers)
    print(binary_numbers)
    print(hexadecimal_numbers)