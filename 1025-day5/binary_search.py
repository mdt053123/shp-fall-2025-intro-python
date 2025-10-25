def binary_search(nums, val):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

nums = [3, 5, 7, 8, 9, 10, 11, 13, 14]

print(binary_search(nums, 11))