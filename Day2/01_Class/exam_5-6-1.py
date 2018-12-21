#부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    
    def PrintInfo(self):
        print("Info(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))
    
    def PrintPersonData(self):
        print("Person(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))

#자식 클래스
# class Student(Person):
#     def __init__(self, name, phoneNumber, subject, studentID):
#         self.Name = name
#         self.PhoneNumber = phoneNumber
#         self.Subject = subject
#         self.StudentID = studentID


# p = Person("Derick", "010-123-4567")
# s = Student("Marry", "010-654-3210", "Computer Science", "990999")

# print(p.__dict__)
# print(s.__dict__)

#자식 클래스 재정의
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.Subject = subject
        self.StudentID = studentID

    def PrintStudentData(self):
        print("Student(Name:{0}, Phone Number:{1}, Subject:{2}, Student ID:{3})".format(self.Name, self.PhoneNumber, self.Subject, self.StudentID))

    def PrintInfo(self):
        Person.PrintInfo(self)
        print("Info(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))

s = Student("Marry", "010-654-3210", "Computer Science", "990999")
s.PrintPersonData()
s.PrintStudentData()
s.PrintInfo()

