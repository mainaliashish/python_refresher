print('\nWelcome To Grade Sorting App.')

grades = []

i = 1
j = 0
item = ['first', 'second', 'third', 'fourth']
for i in range(1,5):
    grade = int(input(f'\nWrite your {item[j]} grade (1-100) : '))
    grades.append(grade)
    i += 1
    j += 1

# print(grades)
print(f'\nYour grades are : {grades}')
grades.sort(reverse=True)
print(f'\nYour grades from highest to lowest are : {grades}')

print('\nThe two lowest grades will be dropped.')
lowest_one = grades.pop()
lowest_two = grades.pop()
print(f'\nRemoved grade: {lowest_one}')
print(f'Removed grade: {lowest_two}')

print(f'\nYour remaining grades are : {grades}')
print(f'Nice Work! Your highest grade is : {grades[0]}')

