import unittest
from employee_classes import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        first_name = 'Alkhair'
        last_name = 'Mohamed'
        my_annual_salary = 5000
        self.my_employee = Employee(first_name, last_name, my_annual_salary)
        self.a_raise = 6000

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 10000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.a_raise)
        self.assertEqual(self.my_employee.annual_salary, 11000)


if __name__ == '__main__':
    unittest.main()

