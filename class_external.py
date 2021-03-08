class Student:
    def __init__(self,name,grade,age,GPA=95):
        self.name = name
        self.grade = grade
        self.age = age
        self.GPA = GPA 
    
    def fun_name(self):
        print("The student's name is " + self.name)


    def print_age(self):
        print("The student's age is " + self.age)

    
    def print_attributes(self):
        print(self.name,self.grade,self.age,self.GPA)