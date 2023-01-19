# for i in range(10):
#     print(i)

teams = ['Gaints', 'Hulk', 'Rainbow', 'Green', 'Lion']

x = 'gaints' in teams
y = 'Gaints' in teams

print(x, y)

for team in teams:
    print(team)

values = [1,3,4,5,7]
sum = 0

for value in values:
    sum += value

print(sum)

my_list = ['Hello', 'world']
new_word = '**'.join(my_list)
print(new_word)

## List Comphrension

numbers = list(range(10, 101, 10))
print(numbers)

square_numbers = [number**2 for number in numbers]
print(square_numbers)

## Loop through Multiple Lists
names = ['jack', 'john', 'mark', 'bill']
ages = [29, 24, 35, 23]

for i in range(len(names)):
    print(f'{names[i].title()} : {ages[i]}')

## Zip() function needs to have same number of items in both lists
## Loop through multiple lists using zip()
print('\nUsing zip() function')
for name, age in zip(names, ages):
    print(f'{name.title()} : {age}')
