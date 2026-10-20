class Student:
    def __init__(self,  name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def display_info(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Grade:",self.grade)

class Undergraduatestudent(Student):
    def __init__(self,name,id,grade,major):
        super().__init__(name,id,grade)
        self.major = major  

    def display_info(self):
        super().display_info()
        print("Major:", self.major)

class Graduatestudent(Student):
    def __init__(self,name,id,grade,program_title):
        super().__init__(name,id,grade)
        self.program_title = program_title

    def display_info(self):
        super().display_info()
        print("Program Title:", self.program_title) 

s1= Student("ali", 1123, 90)
s2= Undergraduatestudent("farag", 2523, 90, "Engineering")   
s3= Graduatestudent("ahmed", 25011, 80, "Master's Program") 

s1.display_info()
s2.display_info()
s3.display_info()