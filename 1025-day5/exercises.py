import random

def count_occurences(nums, val):
    """
    Return the number of times
    val appears in nums (0 if none)
    """
    count = 0
    
    return count
    
def selection_descending(nums):
    """
    Run selection sort in descending order
    """
    n = len(nums)
    
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
    
nums = [random.randint(-10, 10) for i in range(20)] # generate 20 random numbers on [-10, 10]