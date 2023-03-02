class animal:
    counter = 0
    reproduction_rate = 0.6
    def __init__(self, name, eat, sciname):
        self.name = name
        self.eat = eat
        self.sciname = sciname
        animal.counter += 1
    def eating(self):
        return f"{self.name} eats {self.eat}"

    def showname(self):
        return f"{self.name} in scitific name is {self.sciname}"

    def adderone(self):
        animal.reproduction_rate *= 2

test1 = animal("crocodile","meat","crocodyile")
test1.adderone()
print(test1.name)
print(test1.eat)
print(test1.sciname)
print(test1.reproduction_rate)