# Exercise 1

def mat_add(M1, M2):
    """
    M1, M2 are 2D lists,
    return a matrix that is M1 + M2;
    if dimensions(M1) != dimensions(M2),
    return None
    
    e.g. [[2, 3], [4, 2]], [[0, 1], [1, 0]] = [[2, 4], [5, 2]]
    """
    
M1 = [[2, 3], [4, 2]]
M2 = [[0, 1], [1, 0]]

M3 = mat_add(M1, M2)

# Exercise 2

def dot(u, v):
    """
    return u dot v, in other words u1v1 + u2v2 + ... + uNvN;
    if len(u) != len(v), return None
    """
    
# Exercise 3

def search(M, target):
    """
    return as a tuple the (row, col) pair
    at which target is found, else (if not found)
    return None
    """