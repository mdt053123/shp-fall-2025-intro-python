fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    
print(list(enumerate(fruits)))

print()

def square(x):
    return x * x

sq = lambda x : x * x

print(square(4))
print(sq(4))
print()

greet = lambda name : f"Hello, {name}!"

print(greet("Michael"))

squares = [sq(x) for x in range(10)]
print()
print(squares)

nums = [n for n in range(50)]
print(nums)
print()

d = { x : x*x for x in range(5) }
print(d)