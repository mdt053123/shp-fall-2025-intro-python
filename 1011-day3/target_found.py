def target_found(l, target):
    """
    This should return True if target is an element of l, False otherwise
    """
    
    for val in l:
        if val == target:
            return True # whenever we return, the function call ends
        
    return False

l = ["apple", 3, False, 9j, 'a']

print(target_found(l, "apple"))
print(target_found(l, 4))