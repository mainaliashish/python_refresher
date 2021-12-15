# LISTS in PYTHON

topics = ['Maths', 'Science', 'Physics', 'Social', 'Computer Science', 'Algebra']

print(topics)
print(type(topics))

topics.append('Arts')
print(topics)

topics.pop()
print(topics)

print(topics[:2])

colors = []

i = 1
for i in range(1,4):
    color = input("Enter a color name : ")
    colors.append(color)
    i += 1

print(colors)