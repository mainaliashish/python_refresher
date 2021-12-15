print('\n************************************************')
print('Welcome To Temperature Conversion Program.')
print('************************************************')

degree_fahrenheit = float(input('\nWhat is the temperature in Degree Fahrenheit: '))

degree_fahrenheit = round(degree_fahrenheit, 4)
degree_celsius = round(((degree_fahrenheit - 32) * 5) / 9, 4)
degree_kelvin  = round(degree_celsius + 273.15, 4)

print(f'Degree Celsius    : \t{degree_fahrenheit} °F')
print(f'Degree Fahrenheit : \t{degree_celsius} °C')
print(f'Degree Kelvin     : \t{degree_kelvin} °K')
