x = 0

while x < 10:
    print(f"Value of x is {x}")
    x = x + 1 # another way of writing this is x += 1
    
print() # prints a blank line

for i in range(10):
    print(f"Value of i is {i}")
    
# Exercise: print 10-15, not inclusive of 15 (e.g. 10, 11, 12, 13, 14)
# Reminder: range(a, b) -> {a, a + 1, ..., b - 2, b - 1} {[a, b)}

print()
print()
print()

n = 10
while n < 15:
    print(f"n = {n}", end=' ')
    n += 1
   
print()

for i in range(10, 15):
    print(f"i = {i}", end=' ')