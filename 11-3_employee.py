
# print(new_salary)
import unittest
from employee_raise import Employee


class TestRaise(unittest.TestCase):
    """Test for the correct salary"""

    def setUp(self):
        """create an employee example for use in all test methods"""
        self.employee0 = Employee('jack', 'smith', 5000)
        self.custom_salary_raise = 6000

    def test_give_default_raise(self):
        self.new_salary = self.employee0.give_raise()
        self.assertEqual(self.new_salary, 10000)

    def test_give_custom_raise(self):
        self.new_salary = self.employee0.give_raise(self.custom_salary_raise)
        self.assertEqual(self.new_salary, 11000)


unittest.main()
