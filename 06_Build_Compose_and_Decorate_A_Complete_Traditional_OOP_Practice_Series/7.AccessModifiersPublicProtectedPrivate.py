class Employee:
    def __init__(self):
        self.name = "John"
        self._salary = 50000
        self.__ssn = "123-45-6789"

e = Employee()
print(e.name)         # Public: accessible
print(e._salary)      # Protected: accessible but discouraged
# print(e.__ssn)      # Private: raises AttributeError
print(e._Employee__ssn)  # Accessing private using name mangling
