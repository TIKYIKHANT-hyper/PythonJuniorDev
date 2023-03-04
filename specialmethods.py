class employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def email(self):
        return f"{self.firstname}{self.lastname}@gmail.com"

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return self.fullname()
test1 = employee("Ko","Kyaw",230000)
test2 = employee("Sa","Naing",310400)
print(test1 + test2)
print(test1.__repr__())