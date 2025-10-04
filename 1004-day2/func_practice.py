def greet(name):
    # greet (print) person with name 'name'
    print(f"Hello, {name}!")
    
def is_even(n):
    # return True if n is even, False if n is odd
    return n % 2 == 0

def add(x, y):
    # return x + y
    return x + y
    
greet("Michael") # should print 'Hello, Michael!'
print(is_even(3), is_even(4)) # should print 'False True'
print(add(3, 4)) # should print '7'