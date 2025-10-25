nums = [3, 4, 7, -1, 99, 12, 3]

def linear_search(nums, val):
    """
    Search through nums, and
    return the index of the first
    occurence of val in nums, or
    -1 if val is not in nums
    """
    
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1


print(linear_search(nums, 3)) # print '0'
print(linear_search(nums, 99)) # print '4'
print(linear_search(nums, 98)) # print '-1'