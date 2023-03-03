import datetime as dt
class company:
    numberofcompanies = 0
    grade = ""
    def __init__(self,id , name, service,numberofemployee):
        self.id = id
        self.name = name
        self.service = service
        self.numberofemployee = numberofemployee
        company.numberofcompanies += 1

    def isregistered(self):
        return self.id > 0

    def countemployee(self):
        return self.numberofemployee

    def typeofservice(self):
        print(f"We offer {self.service}")

    def showname(self):
        return self.name

    @classmethod
    def setgrade(cls,inputstr):
        cls.grade = inputstr

    @staticmethod
    def registerdate():
        return dt.datetime.now()

class companybranch(company):
    def __init__(self,id , name, service,numberofemployee,subid,subname):
        super().__init__(id , name, service,numberofemployee)
        self.subid = subid
        self.subname = subname
    def showbranch(self):
        return f"{self.subid} {self.subname} under {self.name}"

class developer(company):
    def __init__(self, id , name, service,numberofemployee,devid, firstname, lastname, programming_language):
        super().__init__(id , name, service,numberofemployee)
        self.devid = devid
        self.firstname = firstname
        self.lastname = lastname
        self.programming_languague = programming_language

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def developerid(self):
        return f"{self.devid}"

    def fav_lang(self):
        return self.programming_languague

test1 = company(1,"Amogus Flim","Fliming",6979)
test2 = companybranch(1,"Amogus Flim","Fliming",6979,1,"Ronaldo")

print(test2.registerdate())
print(test1.service)
print(help(company))
print(help(companybranch))