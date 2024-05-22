class User:
    def __init__(self, first_name, last_name, **information):
        self.information = information
        self.information['First name'] = first_name
        self.information['Last name'] = last_name

    def describe_user(self):
        for key, info in self.information.items():
            print(f'{key}: {info}')

    def greet_user(self):
        print(f''
              f'Welcome back {self.information['First name']} {self.information['Last name']}\n')


user = User('Alkhair', 'Mohamed', username='amaam2004', age=19)
user.describe_user()
user.greet_user()

user = User('Mohamed', 'Ali', username='theonetheonly')
user.describe_user()
user.greet_user()

