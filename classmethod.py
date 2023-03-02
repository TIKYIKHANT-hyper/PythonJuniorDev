import datetime
class student:
    total_students = 0
    role_num = 0
    def __init__(self,firstname,lastname,id,age,email):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.age = age
        self.email = email
        student.total_students += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def Email(self):
        return f"{self.email}"

    @classmethod
    def stdstr(cls,inputstr):
        firstname , lastname , id , age , email = inputstr.split("-")
        return cls(firstname,lastname,id,age,email)

    @classmethod
    def set_role_num(cls,rolenum):
        cls.role_num = rolenum

    #corey schafer's example
    @staticmethod
    def is_schoolday(date):
        if date.weekday() == 0 or date.weekday() == 6:
            return False
        return True
student1 = student("Min Ko","Naing",1,18,"minkonaingt2@gmail.com")
student2 = student("Kyaw Swar","Win",2,19,"kyawswar26@gmail.com")
student3str = "Shin Thant-Aung-3-19-shine64@gmail.com"
student3 = student.stdstr(student3str)

print(student1.fullname())
print(student2.Email())
print(student3.fullname())
real = datetime.date(2020,8,16)
print(student1.is_schoolday(real))