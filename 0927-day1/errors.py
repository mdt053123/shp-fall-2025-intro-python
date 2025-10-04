#print(name) # NameError -> variable doesn't exist

name = "Kevin"
print(name)

#print("Hello" # SyntaxError -> some typo or syntax mistake

print("Hello")

#age = "16"
#print(age + 5) # TypeError -> mismatch in variable types

age = "16"
print(int(age) + 5)

# LOGIC ERROR
birth_year = 2004
age = 2025 + birth_year
print(age)