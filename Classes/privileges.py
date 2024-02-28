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
        self.privileges = Privileges(privileges)


class Privileges:

    def __init__(self, privilege_list):
        self.privilege_list = privilege_list

    def show_privileges(self):
        print('privileges')
        for privilege in self.privilege_list:
            print(f'\t{privilege}')


privileges = ['can add post', 'can delete post', 'can ban users']

admin = Admin('L', 'M', 20)
admin.describe_user()
admin.privileges.show_privileges()
