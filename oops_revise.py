class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f'Config is : {self.cpu}, {self.ram}')

# Constructor is used to assign values at the time of Object creation
# __init__ method is used as constructor in python

class Phone:
    def __init__(self, name, game_name):
        self.name = name
        self.game_name = game_name
        # pass

    def set_color(self, color):
        self.color = color
    
    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color
    
    def show_cost(self):
        return self.cost

    def make_call(self):
        print(f'I can make a call to {self.name}')

    def play_game(self):
        print(f'Loading game {self.game_name}.. Please wait ..')

phone1 = Phone('Ashok', 'Ludo')
phone1.play_game()
phone1.make_call()
phone1.set_color('red')
color = phone1.show_color()
print(color)

# Object Creation
computer_1 = Computer('i5', '8GB')
computer_2 = Computer('Ryzen 3000', '16GB')

# Computer.config(computer_1)
# Computer.config(computer_2)

computer_1.config()
computer_2.config()


# Constructor Method in Python

class Employee:
    def __init__(self, name, age, gender, job, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
        self.salary = salary

    def get_user_info(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Gender : {self.gender}')
        print(f'Job : {self.job}')
        print(f'Salary : {self.salary}')
    
    @staticmethod
    def show_role(cls):
        print('I am a Employee')

class Student(Employee):
    def show_role(self):
        print('I am a student')

ram = Student('Ram', 28, 'Male', 'Web Developer', 50000)
ram.get_user_info()
ram.show_role()



