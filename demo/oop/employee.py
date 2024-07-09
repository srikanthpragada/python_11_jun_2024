class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name  : {self.name}")
        print(f"Salary: {self.salary}")

    def getNetSalary(self):
        hra = self.salary * 30 // 100
        da  = self.salary * 15 // 100
        gross = self.salary + hra  + da
        tax = gross * 10 // 100
        return gross - tax

e = Employee("Jack", 55000)
e.show()
print(e.getNetSalary())
