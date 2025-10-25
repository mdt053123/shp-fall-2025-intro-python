def foo(nums):
    x = nums[0]
    
    for num in nums:
        if num < x:
            x = num
            
    return x

nums = [3, -5, 2, 4, 9, 9]

print(foo(nums))

def bar(nums):
    x = 0
    
    for i in range(len(nums)):
        if nums[i] < nums[x]:
            x = i
            
    return x

print(bar(nums))

print()
print(f"min(nums) = nums[{bar(nums)}] = {foo(nums)}")

def baz(nums):
    return nums[bar(nums)]

print(foo(nums) == baz(nums))

idx = bar(nums)

def find_max(nums):
    max_num = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            
    return max_num

def find_max_idx(nums):
    max_idx = 0
    
    for i in range(1, len(nums)):
        if nums[i] > nums[max_idx]:
            max_idx = i
            
    return max_idx

print()
print(find_max(nums))
print(find_max_idx(nums))