import random

def count_occurences(nums, val):
    """
    Return the number of times
    val appears in nums (0 if none)
    """
    count = 0
    
    for num in nums:
        if num == val:
            count += 1
    
    return count
    
def selection_descending(nums):
    """
    Run selection sort in descending order
    """
    n = len(nums)
    
    for i in range(n - 1):
        max_idx = i
        
        for j in range(i + 1, n):
            if nums[j] > nums[max_idx]:
                max_idx = j
                
        nums[i], nums[max_idx] = nums[max_idx], nums[i]
        
    return nums


# DO NOT ATTEMPT UNTIL DONE WITH FIRST TWO

def binary_search(nums, val):
    return binary_search_helper(nums, val, 0, len(nums) - 1)

def binary_search_helper(nums, val, left, right):
    """
    Hint, if nums[mid] == val, return mid;
    if nums[mid] < val, return binary_search_helper with left = mid + 1;
    elif nums[mid] > val, return binary_search_helper with right = mid -1;
    else return -1
    """
    mid = (left + right) // 2
    
    if left > right:
        return -1
    if nums[mid] == val:
        return mid
    elif nums[mid] < val:
        return binary_search_helper(nums, val, mid + 1, right)
    elif nums[mid] > val:
        return binary_search_helper(nums, val, left, mid - 1)
    
nums = [random.randint(-10, 10) for i in range(20)] # generate 20 random numbers on [-10, 10]
print(count_occurences(nums, 2))
sorted_desc = selection_descending(nums)
print(sorted_desc)
sorted_asc = sorted(nums)
print(sorted_asc)
print(binary_search(sorted_asc, 10))
