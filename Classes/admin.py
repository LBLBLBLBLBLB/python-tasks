class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'user name is {self.first_name}, surname is {self.last_name} and age is {self.age}')

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban users']

    def show_privileges(self):
        print('admin privileges')
        for privilege in self.privileges:
            print(f'\t{privilege}')


admin = Admin('L', 'M', 20)
admin.describe_user()
admin.show_privileges()
