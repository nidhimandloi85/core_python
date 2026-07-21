class Student:
    def __int__(self):
        self.name=""
        self.age=0
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_age(self,age):
        self.age=age
    def get_age(self):
        return self.age
class Course:
    def __init__(self):
        self.course=""
        self.branch=""
    def set_course(self,course):
        self.course=course
    def get_course(self):
        return self.course
    def set_branch(self,branch):
        self.branch=branch
    def get_branch(self):
        return self.branch
class Clg(Student,Course) :
    pass
c=Clg()
c.set_name("nidhi")
c.set_age(19)
c.set_course("bca")
c.set_branch("cs")
print("name:",c.get_name())
print("age :",c.get_age())
print("course :",c.get_course())
print("branch:" ,c.get_branch())
