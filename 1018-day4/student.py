class Student:
    def __init__(self, name, grade, missing_assignments):
        self.name = name
        self.grade = grade
        self.missing_assignments = missing_assignments
    
    def get_info(self):
        return f"Student Name: {self.name}\nGrade: {self.grade}\nNum. of Assignments Missing: {self.missing_assignments}"

    def advance(self):
        if self.missing_assignments <= 3:
            self.grade += 1
            self.missing_assignments = 0
            print(f"Student has advanced from grade {self.grade - 1} to grade {self.grade}")
        else:
            print(f"Student has {self.missing_assignments} missing assignments, cannot pass yet")
    
    def __str__(self):
        return f"({self.name}, {self.grade}, {self.missing_assignments})"
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "grade":
            return self.grade
        elif key == "missing_assignments":
            return self.missing_assignments
        else:
            return None
        
    def __eq__(self, other):
        return self.name == other.name and self.grade == other.grade and self.missing_assignments == other.missing_assignments
            
student_1 = Student("Michael", 10, 2) # invoking 'constructor' (__init__)
student_2 = Student("Bob", 11, 4)
student_3 = Student("Alice", 9, 1)

# print(student_1.get_info())
# print()
# student_1.advance()
# print()
# print(student_1.get_info())
# print()
# print(type(student_1))

students = [student_1, student_2, student_3]

student_4 = Student("Jerry", 12, 8)
students.append(student_4)

for student in students:
    print(student["a"])
    
student_5 = Student("Michael", 10, 2)

print(student_1 == student_5)
print(student_1.__eq__(student_5))