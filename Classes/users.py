class User:
    def __init__(self, first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'user name is {self.first_name}, surname is {self.last_name} and age is {self.age}')

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')


user1 = User('John', 'Wick', 40)

user1.describe_user()
user1.greet_user()