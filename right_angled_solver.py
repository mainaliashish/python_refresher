import math
print('\nWelcome to the Right Angled Triangle Solver App.')

side_a = float(input('\nPlease enter the first leg of the triangle: '))
side_b = float(input('Please enter the second leg of the triangle: '))

side_a = round(side_a, 3)
side_b = round(side_b, 3)
side_c = math.sqrt(side_a ** 2 + side_b ** 2)
side_c = round(side_c, 3)
area_of_triangle = 0.5 * side_a * side_b
area_of_triangle = round(area_of_triangle, 3)

print(f'The first leg of the triangle is {side_a} and second leg is {side_b}')
print(f'The third leg of the triangle is {side_c}')
print(f'The area of the triangle is {area_of_triangle}')
