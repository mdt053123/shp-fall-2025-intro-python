def f(x):
    x = 2
    return x
    
x = 3
f(x)

print(f(x))
print(x)

y = 4
print(y)

def g():
    global y
    y = 3

g()
print(y)