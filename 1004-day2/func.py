def f(x):
    return 3*x + 4

f(3) # nothing happens, as no print statement

x = 3
y = f(3)

print(f"(x, y) = ({x}, {y})")

print()

for i in range(10):
    print(f"f({i}) = {f(i)}", end=' ')
    
print()

def foo():
    print("foo")
    print("bar")

foo()

x = foo() # x stores 'None'
print(x)

print()

def bar(x, y, z):
    return x*y + z

print(f"bar(3, 1, 2) = {bar(3, 1, 2)}")

print()

def baz(x, y):
    return x+y, x*y

print(baz(3, 2))

print()




def g(x, y, z):
    if x + y == z:
        return z
    else:
        return x, y
    
print(g(1, 2, 3))
print(g(1, 2, 4))