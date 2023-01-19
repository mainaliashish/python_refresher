print('Welcome to Letter Counter App.')

full_name = input("Please enter your full name : ").title().strip()
print(f'Hello {full_name}!')
print('I will count the number of times that a specific letter occur in a message.')

message = input("Please enter your message: ")
message = message.lower().strip()

letter_to_count = input("Please enter a letter to count: ")
letter_to_count = letter_to_count.lower()

total_counts = message.count(letter_to_count)

print(f'{full_name}, Your message has {total_counts} {letter_to_count}\'s in the message.')