def first_index(l, val):
    """
    returns index of first occurence of val in l,
    otherwise -1 if not found
    """
    
    for i in range(len(l)):
        if l[i] == val:
            return i
    
    return -1
            
l = [3, 3, 4, 5, 5, 5, 7]

for num in l:
    print(first_index(l, num))
    
print(first_index(l, 8))