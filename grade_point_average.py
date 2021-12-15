print('\nWelcome to the Grade Point Average Calculator App.')

full_name = input('👤 What is your name:').title().strip()
grade_number = int(input('How many grades would you like to enter: '))

grades = []
for grade in range(1, grade_number+1):
    user_grade = int(input('Enter your grade : '))
    grades.append(user_grade)

grades.sort(reverse=True)
print('\nGrades from Highest to Lowest:')
for grade in grades:
    print(f'\t{grade}')

average_grade = sum(grades) / len(grades)
average_grade = round(average_grade, 2)

print(f'\n{full_name}\'s Grade Summary:')
print(f'\tTotal number of grades: {len(grades)}')
print(f'\tHighest grade: {max(grades)}')
print(f'\tLowest grade: {min(grades)}')
print(f'\tAverage grade: {average_grade}')

desired_average = float(input('\nWhat desired average do you want to get: '))
grade_required = desired_average * (len(grades) + 1) - sum(grades)
grade_required = round(grade_required, 2)

print(f'Good Luck {full_name}!')
print(f'You will need {grade_required} on your next assignment to earn {desired_average}')

# new_grades = grades.copy()
new_grades = grades[:]
print('\nLet\'s see what your grade could have be if you did better/worse in an assignment.')

grade_to_change = int(input('What grade do you like to change: '))
new_grades.remove(grade_to_change)
new_grade_to_add = int(input(f'What grade would you like to change {grade_to_change} to :'))
new_grades.append(new_grade_to_add)

new_grades.sort(reverse=True)
print('\nNew Grades from Highest to Lowest:')
for grade in new_grades:
    print(f'\t{grade}')

new_average_grade = sum(new_grades) / len(new_grades)
new_average_grade = round(new_average_grade, 2)
print(f'\n{full_name}\'s Grade Summary:')
print(f'\tTotal number of grades: {len(new_grades)}')
print(f'\tHighest grade: {max(new_grades)}')
print(f'\tLowest grade: {min(new_grades)}')
print(f'\tAverage grade: {new_average_grade}')

print(f'\nYour new average would be {new_average_grade} compared to the real average of {average_grade}')
average_change = new_average_grade - average_grade
average_change = round(average_change, 2)
print(f'This is a change of {average_change} points.')

print('\nToo bad. Your original grades are stil same.')
print(grades)
print('You should go ask for extra credit.')
