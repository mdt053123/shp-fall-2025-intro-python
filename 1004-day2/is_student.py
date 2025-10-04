age = int(input("Enter your age: "))
is_student = input("Are you a student (enter 'y' or 'n'): ")

if (age >= 18 and age <= 24) and is_student == 'y':
    print("You are a college student")
elif (age >= 14 and age < 18) and is_student == 'y':
    print("You are a high school student")
else:
    print("You are not a student")