# Day 6: NumPy & Pandas

## Topics Covered

### 1. Comprehensive Review
- Input/output, variables, types
- Conditionals, loops, functions
- Lists, tuples, sets, dictionaries
- Classes and lambda functions

### 2. NumPy Arrays
NumPy provides efficient numerical arrays.

```python
import numpy as np

arr = np.array([3, 2, 5, 6, 8])
arr.sort()
np.median(arr)
```

### 3. 2D Arrays (Matrices)
```python
M = [[3, 2, 1],
     [1, 4, 7],
     [4, 9, -2]]

M[0]     # first row: [3, 2, 1]
M[0][1]  # element at row 0, col 1: 2
```

#### Iterating Over Matrices
```python
# Using nested for-each
for row in M:
    for num in row:
        print(num, end=' ')

# Using indices
for r in range(len(M)):
    for c in range(len(M[r])):
        print(M[r][c], end=' ')
```

### 4. NumPy Matrix Operations
```python
mat = np.array([[2, 4], [3, 6]])
```

### 5. Pandas Series
One-dimensional labeled array.

```python
import pandas as pd

scores = pd.Series([90, 85, 88], index=['Alice', 'Bob', 'Charlie'])
scores['Alice']  # 90
scores[0]        # 90
```

### 6. Pandas DataFrame
Two-dimensional labeled data structure.

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [90, 85, 88],
    'Age': [20, 21, 19]
}
df = pd.DataFrame(data)
```

#### DataFrame Operations
| Method | Description |
|--------|-------------|
| `df.head()` | First 5 rows |
| `df.tail()` | Last 5 rows |
| `df.describe()` | Summary statistics |
| `df['Column']` | Select single column |
| `df[['A', 'B']]` | Select multiple columns |
| `df[df['Score'] > 86]` | Filter rows |

## Exercises
- **mat_add** - Add two matrices
- **dot** - Calculate dot product of two vectors
- **search** - Find target value in matrix, return (row, col)

