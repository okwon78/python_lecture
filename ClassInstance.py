class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def private_info(self):
        return f"name: {self.name}, age: {self.age}"

    
emp1 = Employee("Kwon", 10, 1000)
emp2 = Employee("Joon", 20, 2000)

print(emp1.name, emp1.age, emp1.salary)
print(emp2.name, emp2.age, emp2.salary)

print(emp1.private_info())
print(Employee.private_info(emp2))
