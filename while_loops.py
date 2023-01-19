
# Check a number is Odd or Even
current_num = 1
while current_num <= 10:
    if current_num % 2 == 0:
        print(f'{current_num} is Even.')
    else:
        print(f'{current_num} is Odd')
    current_num += 1

numbers = list(range(1,20))
# print(numbers)
# exit(0)
while numbers:
    numbers.pop()
    print(numbers)
print('All Elements removed')
exit(0)

numbers = [4,1,3,2,4,5,4,4,4,6,7,8,4,3,5,6,7,2,1,4,5]
while 4 in numbers:
    numbers.remove(4)
    print(numbers)
print('All 4\'s has been removed')
exit(0)


current_num = 1
flag = True
while flag:
    current_num = int(input('Please enter a number : '))
    if current_num % 3 == 0:
        print(f'{current_num} is divisible by 3.')
    else:
        print(f'{current_num} is not divisible by 3.')
    
    choice = input('Enter n to stop or press Enter to continue:')
    if choice.lower().startswith('n'):
        flag = False
    else:
        flag = True

print('Quitting...')