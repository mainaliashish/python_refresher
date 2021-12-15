print('Welcome to MPH to MPS Conversion App.')

miles_per_hour = input('Please enter your speed in Miles per hour: ')
miles_per_hour = float(miles_per_hour)

meters_per_second = round(miles_per_hour / 2.237, 2)

print(f'Your speed in meters per second is {meters_per_second}')

