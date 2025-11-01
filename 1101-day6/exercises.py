# Exercise 1

def mat_add(M1, M2):
    """
    M1, M2 are 2D lists,
    return a matrix that is M1 + M2;
    if dimensions(M1) != dimensions(M2),
    return None
    
    e.g. [[2, 3], [4, 2]], [[0, 1], [1, 0]] = [[2, 4], [5, 2]]
    """
    
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        return None
    
    M3 = []
    
    for r in range(len(M1)):
        new_row = []
        for c in range(len(M1[0])):
            new_row.append(M1[r][c] + M2[r][c])
        M3.append(new_row)
    
    return M3
    
M1 = [[2, 3], [4, 2]]
M2 = [[0, 1], [1, 0]]

M3 = mat_add(M1, M2)
print(M3)

# Exercise 2

def dot(u, v):
    """
    return u dot v, in other words u1v1 + u2v2 + ... + uNvN;
    if len(u) != len(v), return None
    """
    
    if len(u) != len(v):
        return None
    
    prod = 0
    
    for i in range(len(u)):
        prod += u[i]*v[i]
        
    return prod

print(dot((3, 2, 5), (4, 1, 0)))

# Exercise 3

def search(M, target):
    """
    return as a tuple the (row, col) pair
    at which target is found, else (if not found)
    return None
    """
    
    for r in range(len(M)):
        for c in range(len(M[r])):
            if M[r][c] == target:
                return (r, c)
            
    return None
    
print(search(M3, 4))