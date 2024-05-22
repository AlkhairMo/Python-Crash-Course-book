from user import User


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts=0, *privileges, **information):
        super().__init__(first_name, last_name, login_attempts, **information)
        self.privileges = privileges

    def show_privileges(self):
        print('This admin privileges are:')
        for privileage in self.privileges:
            print(f'- {privileage}')
