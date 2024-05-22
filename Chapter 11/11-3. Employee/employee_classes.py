class Employee:
    def __init__(self, f_name, l_name, annual_salary):
        self.f_name = f_name
        self.l_name = l_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        self.annual_salary = self.annual_salary + raise_amount


