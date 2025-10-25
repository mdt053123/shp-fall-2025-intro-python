class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
    def __eq__(self, other): # overloads '=='
        return self.name == other.name and self.grade == other.grade
        
s1 = Student("Michael", 94)
print(s1.get_grade())

s2 = Student("Michael", 94)

print(s1 == s2)
print(s1 is s2)
print(s1.__eq__(s2))