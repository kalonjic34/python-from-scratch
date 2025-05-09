class Student():
    def __init__(self,math,history,writing):
        self.math = math
        self.history = history
        self.writing = writing
        
    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student):
        return self.grades == other_student.grades
    
    def __gt__(self,other_student):
        return self.grades > other_student.grades
    
    def __le__(self, other_student):
        return self.grades <= other_student.grades
    
    def __add__(self, other_student):
        return self.grades + other_student.grades
    
    def __sub__(self, other_student):
        return self.grades - other_student.grades
    
bob = Student(math=90,history=90,writing=90)
matt = Student(100,90,80)
joe = Student(math=40,history=45,writing=50)

print(bob == matt)
print(matt == bob)
print(matt > joe)
print(joe <= bob)
print(bob + matt)
print(matt - joe)
print(bob == matt)