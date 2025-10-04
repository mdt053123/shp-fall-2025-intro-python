x = 0

while True:
    print(f"x = {x}", end=' ')
    x += 1
    
    if x == 10:
        break

print()

x = 0

while True:
    if x == 10:
        break
    
    x += 1
    print(f"x = {x}", end=' ')