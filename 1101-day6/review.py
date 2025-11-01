# First Topic - Input, Output, Variables, Types, Operations

x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))

print(x + y)

# Second Topic - Conditionals, Loops, Functions

user_grade = int(input("Enter a grade: "))

if user_grade >= 90:
    print("A")
elif user_grade < 90 and user_grade >= 80:
    print("B")
else:
    print("C or Lower")
    
x = int(input("Enter a positive number or -1 to stop: "))

while True: # equiv. to 'while x != -1'
    if x == -1:
        break
    print(x)
    x = int(input("Enter a positive number or -1 to stop: "))
    
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num, end=' ')

print()

def foo(x):
    return x * x

bar = lambda x : x * x

print(foo(3))
print(bar(3))

baz = lambda x, y : x * y

print(baz(2, 3))

qux = lambda x, y : (y, x)

x = 3
y = 2

u, v = qux(x, y) # tuple 'unpacking'

print(qux(x, y))
print(u, v)

# Lists, Tuples, Sets, Dicts
l = [3, 2, 4, 5, 6]
second_elem = l[1]
x = l[-1]

t = (3, 2)

s = {3, 2, 4, 4, 7}

d = { "Michael" : "pizza",
      "Bob" : "burger",
      "Alice" : "sushi" }

print(d["Alice"])

# Classes and Objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def print_point(self):
        print((x, y))
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
p1 = Point(3, 2)
p2 = Point(3, 2)
print(p1 == p2)
p1.print_point()