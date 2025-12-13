# Day 3: Data Structures

## Topics Covered

### 1. Lists
Ordered, mutable collections.

```python
nums = [1, 3, 5, 7, 9]
```

#### Common List Operations
| Method | Description |
|--------|-------------|
| `nums[i]` | Access element at index i |
| `nums[-1]` | Access last element |
| `nums.append(x)` | Add x to end |
| `nums.pop()` | Remove & return last element |
| `nums.pop(i)` | Remove & return element at index i |
| `nums.insert(i, x)` | Insert x at index i |
| `nums.remove(x)` | Remove first occurrence of x |
| `nums.index(x)` | Get index of first occurrence of x |
| `nums.sort()` | Sort in place |
| `len(nums)` | Get length |

#### Three Ways to Iterate
```python
# Method 1: while loop
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

# Method 2: for loop with range
for i in range(len(nums)):
    print(nums[i])

# Method 3: for-each loop
for num in nums:
    print(num)
```

### 2. Tuples
Ordered, **immutable** collections.

```python
t = (3, 4, 5)
x, y, z = t  # unpacking
```

- Use `(value,)` for single-element tuples
- Often used for coordinates: `point = (2, 1)`

### 3. Sets
Unordered collections of **unique** values.

```python
s = {3, 4, 5, 5, 6}  # stores {3, 4, 5, 6}
```

#### Set Operations
| Method | Description |
|--------|-------------|
| `s.add(x)` | Add element |
| `s1.intersection(s2)` | Elements in both sets |
| `s1.union(s2)` | Elements in either set |
| `s1.difference(s2)` | Elements in s1 but not s2 |
| `s2.issubset(s1)` | Check if s2 ⊆ s1 |

### 4. Dictionaries
Key-value pairs.

```python
phone_book = {
    'Michael': '9145551234',
    'Bob': '2031295567'
}
```

#### Dictionary Operations
| Method | Description |
|--------|-------------|
| `d[key]` | Get value for key |
| `d.get(key)` | Get value (returns None if missing) |
| `d.keys()` | Get all keys |
| `d.values()` | Get all values |
| `d.items()` | Get all (key, value) pairs |
| `d[key] = val` | Set/update value |

## Exercises
- **first_index.py** - Find first occurrence of value in list
- **target_found.py** - Check if target exists in list
- **print_reverse.py** - Print list elements in reverse
- **exercises.py** - Value counts, fake dict implementation, grade tracker

