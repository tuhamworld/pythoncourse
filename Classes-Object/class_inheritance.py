from datetime import date

class Employee:
    minimum_wage = 3000

    # Defining Class methods
    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is Bankrupt.")
        cls.minimum_wage = new_wage


    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)


# Class Inheritance 
class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")

class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework



    def increase_salary(self, percent, bonus=0):
        # self.salary += self.salary * (percent/100)
        super().increase_salary(percent)
        self.salary += bonus


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-soo", 38, 1000, "Flask")

e = Employee.new_employee("Mary", date(1991, 8, 12))

# print(employee2.name)
# print(employee2.framework)
# print(Employee.__dict__)
# print(Employee.minimum_wage)
# Employee.change_minimum_wage(2500)
# print(Employee.minimum_wage)
# Employee.change_minimum_wage(3500)
# print(Employee.minimum_wage)

print(e.name)
print(e.age)
print(e.salary)