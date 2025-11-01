M = [[3, 2, 1],
     [1, 4, 7],
     [4, 9, -2]]

print(M[0])
print(M[0][1])
print()

for row in M:
    for num in row:
        print(num, end=' ')
    print()
    
print()

for r in range(len(M)):
    for c in range(len(M[r])):
        print(M[r][c], end=' ')
    print()