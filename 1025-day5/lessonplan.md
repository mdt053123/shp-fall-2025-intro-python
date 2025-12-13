# Day 5: Searching, Sorting & Functional Programming

## Topics Covered

### 1. Finding Min/Max
```python
def find_min(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

def find_min_idx(nums):
    min_idx = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[min_idx]:
            min_idx = i
    return min_idx
```

### 2. Linear Search
Search through each element one by one. **O(n)** time complexity.

```python
def linear_search(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1
```

### 3. Binary Search
Only works on **sorted** lists. **O(log n)** time complexity.

```python
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
```

### 4. Selection Sort
Find minimum, swap to front, repeat. **O(n²)** time complexity.

```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
```

### 5. Lambda Functions
Anonymous (unnamed) functions for simple operations.

```python
# Regular function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x

# Multiple parameters
add = lambda x, y: x + y
```

### 6. List Comprehensions
Concise way to create lists.

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i * i)

# List comprehension
squares = [i * i for i in range(10)]

# With condition
evens = [i for i in range(20) if i % 2 == 0]
```

## Exercises
- **r1.py** & **r2.py** - Review finding min/max values and indices
- **exercises.py** - Count occurrences, descending selection sort, recursive binary search

