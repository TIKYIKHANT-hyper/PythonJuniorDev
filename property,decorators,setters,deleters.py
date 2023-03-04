class employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return self.fullname()

    @property
    def email(self):
        return f"{self.firstname}{self.lastname}@gmail.com"

    @fullname.setter
    def fullname(self , name):
        first , last = name.split(" ")
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None

test1 = employee("Ko","Kyaw",230000)
test2 = employee("Sa","Naing",310400)
print(test1.fullname)
test2.fullname = "Min Ko"
print(test2.email)