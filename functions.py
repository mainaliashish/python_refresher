## Functions in python
def add(a, b):
    return a+b

print(add(4,5))

def hello_world():
    pass

def cal_age(age=0, interval=10):
    """Calculate a person's age in x years"""
    print(f'You are currently {age} years old.')
    print(f'In {interval} years, you will be {age+interval} years old.')

cal_age()
cal_age(10, 20)
