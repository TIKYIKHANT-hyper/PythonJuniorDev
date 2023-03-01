class animal:
    def __init__(self, name, eat, sciname):
        self.name = name
        self.eat = eat
        self.sciname = sciname

    def eating(self):
        return f"{self.name} eats {self.eat}"

    def showname(self):
        return f"{self.name} in scitific name is {self.sciname}"


t1 = animal('crocodile', 'meats', 'Crocodylidae')
t2 = animal("hawk","meats","Buteo")
t3 = animal("rabbit","vegetables","Oryctolagus cuniculus")

print(t1.eating())
print(t2.showname())
print(animal.showname(t3))

