nums = [1, 3, 5, 7, 9]

print(nums)

print(type(nums))

print(f"Element at index 0 is {nums[0]}") # nums[0] == 1

nums.append(11)

print(nums)

print(len(nums))

# iteration, 3 ways

index = 0

while index < len(nums):
    print(nums[index], end=' ')
    index += 1

print()

for i in range(len(nums)):
    print(nums[i], end=' ')
    
print()

for num in nums:
    print(num, end=' ')
    
print()
print(nums[-1])
print(nums[-2])
print(nums[-len(nums)]) # len(nums) == 6, -len(nums) == -6, nums[-len(nums)] == nums[-6] => nums[-len(nums)] == nums[0]

nums.pop() # remove the last element
print(nums)

nums.pop(3) # removes the element at index 3
print(nums)

nums.insert(3, 7) # insert(index, element)
print(nums)

nums.remove(3) # remove the element 3
print(nums)

print(nums.index(7)) # gets the index of element 7

print()

values = [-5, 17, 12, 15, -37, 8, 100]
values.sort()
print(values)

print()

colors = ["red", "blue", "green"]

for color in colors:
    print(color)
    
mixed = [3, "apple", True, 4j] # 4j is the complex number 4i
for value in mixed:
    print(type(value))