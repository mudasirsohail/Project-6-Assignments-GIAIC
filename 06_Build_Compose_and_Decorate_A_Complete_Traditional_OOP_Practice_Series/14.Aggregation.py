class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

e = Employee("John")
d = Department("HR", e)
print(d.employee.name)
