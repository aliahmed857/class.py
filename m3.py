class Student:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.id)

class Undergraduatestudent(Student):
    def __init__(self, name, id, major):
        super().__init__(name, id)
        self.major=major

    def display_info(self):
        super().display_info()
        print("Major:", self.major)

class Graduatestudent(Student):
    def __init__(self, name, id, program_title):
        super().__init__(name, id)
        self.program_title=program_title

    def display_info(self):
        super().display_info()
        print("Program Title:", self.program_title)

s1=   Undergraduatestudent("Ali", 1123, "Engineering")
s2=    Graduatestudent("Ahmed", 25011, "Master's Program")  

s1.display_info()
print()
s2.display_info()
                            
