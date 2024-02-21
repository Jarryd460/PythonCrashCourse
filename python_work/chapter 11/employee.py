class Employee:

    def __init__(self, firstname, lastname, annualSalary):
        self.firstname = firstname
        self.lastname = lastname
        self.annualSalary = annualSalary

    def give_raise(self, salaryIncrease = 5_000):
        self.annualSalary += salaryIncrease