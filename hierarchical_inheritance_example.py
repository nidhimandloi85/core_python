class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
class Student(Person) :
    def __init__(self,Class_name="",rollno=0,name="",age=0):
        self.Class_name=Class_name
        self.rollno=rollno
        super().__init__(name,age)
    def get_Class_name(self):
        return self.Class_name
    def get_rollno(self):
        return self.rollno
class Teacher(Person):
    def __init__(self,teach_subject="",name="",age=0):
        self.teach_subject=teach_subject
        super().__init__(name,age)
    def get_teach_subject(self):
        return  self.teach_subject
s=Student("12th",101,"nidhi",19)
print("student")
print("name :",s.get_name())
print("age :",s.get_age())
print("Class:",s.get_Class_name())
print("rollno :",s.get_rollno())
print("-------------------------------------")
t=Teacher("Hindi","tushar",24)
print("teacher")
print("name :",t.get_name())
print("age :",t.get_age())
print("teaching :",t.get_teach_subject())





