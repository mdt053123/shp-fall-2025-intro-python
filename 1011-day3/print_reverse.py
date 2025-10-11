def print_reverse1(l):
    """
    print each element of l in reverse order
    """
    
    idx = len(l) - 1 # last index of l
    
    while idx >= 0:
        print(l[idx], end=' ')
        idx -= 1
    
def print_reverse2(l):
    for idx in range(-1, -len(l) - 1, -1):
        print(l[idx], end=' ')
    
l = [3, 4, 7, 9, 12]
print_reverse1(l)
print()
print_reverse2(l)
print()
l.reverse()
print(l)