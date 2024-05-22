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


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts=0, *privileges, **information):
        super().__init__(first_name, last_name, login_attempts, **information)
        self.privileges = privileges

    def show_privileges(self):
        print('This admin privileges are:')
        for privileage in self.privileges:
            print(f'- {privileage}')
