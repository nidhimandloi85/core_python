class Student:
    def get_student(self):
        self.name=input("name:")
        self.age=input("age:")
        self.gender=input("gender:")
class Test(Student):
    def get_marks(self):
        self.studentClass=input("class :")
        print("enter th marks respective subject :")
        self.hindi=int(input("hindi :"))
        self.english=int(input("english :"))
        self.maths=int(input("maths :"))
class Marks(Test):
    def display(self):
        print("name :", self.name)
        print("age:", self.age)
        print("gender :", self.gender)
        print("class:", self.studentClass)
        print("hindi :", self.hindi)
        print("english :", self.english)
        print("maths :", self.maths)
        total_marks=self.hindi+self.english+self.maths
        if total_marks>100:
            print("passed",total_marks)
        else:
            print("fail",total_marks)
m=Marks()
m.get_student()
m.get_marks()
m.display()


