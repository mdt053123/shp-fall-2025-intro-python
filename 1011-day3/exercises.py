def value_counts(values):
    """
    return a dict containing the number of times each value appears in values,
    i.e. if values == [3, 3, 4, 5, 5, 5, 7], you should return
    { 3 : 2, 4 : 1, 5 : 3, 7 : 1 }
    
    Note that values will contain generic value types (int, str, etc.),
    so each pair in the dict should be some generic type as the key, and
    an int value corresponding to said key
    """
    
    unique_vals = set(values)
    counts = {}
    
    for val in unique_vals:
        counts[val] = values.count(val)
        
    return counts
    
def get(fake_dict, fake_key):
    """
    take in 'fake dict', i.e. [(3, 2), (4, "apple")]
    and return the value associated with 'fake_key', so
    if fake_key == 4, return "apple";
    if fake_key does not exist, return None
    """
    
    for pair in fake_dict:
        if pair[0] == fake_key:
            return pair[1]
    
    return None
    
def add_grade(student_grades, student, grade):
    """
    student_grades records all grades for each student, i.e.
    student_grades == { "Bob" : [33, 97, 80], "Alice": [99, 100] }
    
    Given a student and a new grade, either add the student and create a list with one grade,
    or if the student exists, add the grade to their corresponding list
    
    If a student doesn't exist, write something like student_grades['Jerry'] = [grade]
    """
    
    if student in student_grades.keys():
        student_grades[student].append(grade)
    else:
        student_grades[student] = [grade]

print(value_counts([3, 3, 4, 5, 7, 7, 7]))
print(get([(3, "apple"), (4, 5)], 3))
print(get([(3, "apple"), (4, 5)], 5))

student_grades = {"Bob": [33, 76], "Alice": [55]}
add_grade(student_grades, "Bob", 99)
print(student_grades)
add_grade(student_grades, "Jerry", 44)
print(student_grades)