class Employee():
    """TO give the employee a raise"""

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        self.salary += salary_raise
        return self.salary
