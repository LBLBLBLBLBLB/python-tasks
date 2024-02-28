class User:
    def __init__(self, first_name, last_name, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'user name is {self.first_name}, surname is {self.last_name} and age is {self.age}')
        print(f'user have {self.login_attempts} attempts')

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'you have {self.login_attempts} attempts')

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('John', 'Wick', 40, 10)

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()


