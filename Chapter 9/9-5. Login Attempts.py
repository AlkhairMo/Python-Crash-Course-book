class User:
    def __init__(self, first_name, last_name, login_attempts=0, **information):
        self.information = information
        self.information['First name'] = first_name
        self.information['Last name'] = last_name
        self.information['Login attempts'] = login_attempts

    def describe_user(self):
        for key, info in self.information.items():
            print(f'{key}: {info}')

    def greet_user(self):
        print(f''
              f'Welcome back {self.information['First name']} {self.information['Last name']}')

    def increment_login_attempts(self):
        self.information['Login attempts'] += 1

    def reset_login_attempts(self):
        self.information['Login attempts'] = 0


user = User('Alkhair', 'Mohamed', username='amaam2004', age=19)
user.greet_user()
user.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()  # 4 times
print('\n')
user.describe_user()
print('\n')
user.reset_login_attempts()
user.describe_user()
