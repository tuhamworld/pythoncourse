class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    # def info(self):
    #     print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)},"
            f"{repr(self.position)}, {repr(self.salary)})"
            )

    @property            
    def salary(self):
        # return f"${self.salary}
        # return round(self.set_salary, 2)
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        else:
            self._salary = salary


employee1 = Employee("Ji-soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)


employee1.salary = 2000
# print(employee1.get_salary())
print(employee1.salary)

# Employee.increase_salary(employee2, 20)
# Employee.info(employee2)

# print('\nAlternatively, you can call them directly..\n')

# employee2.increase_salary(20)
# employee2.info()

# print(str(employee1))
# print(repr(employee1))
