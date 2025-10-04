def f(x):
    print(g(x))
    
    
def g(x):
    return x*x

f(3)

def u(v, x):
    print(v(x))
    
def v(x):
    return x*x

u(v, 3)