status = True
print(status)
print(type(status))

# while status:
#     for i in range(4):
#         print('Success.')
#     status = False

if status:
    print('Online')
else:
    print('Offline')

# Break, Continue and Pass
# continue will stop the current loop and start loop again
# break will stops the whole loop
# pass passes over the loops and contine 
for i in range(1,10):
    if i == 5:
        continue
        print(f'Your number is {i}')
    else:
        print(f'{i}')
print('Hello.')