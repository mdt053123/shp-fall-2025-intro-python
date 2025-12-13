# Day 2: Control Flow & Functions

## Topics Covered

### 1. Review
- Variables, types, input/output
- Type casting

### 2. Conditionals
```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code
```

### 3. Comparison Operators
| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

### 4. Logical Operators
- `and` - both conditions must be true
- `or` - at least one condition must be true
- `not` - inverts the condition

### 5. Loops

#### While Loop
```python
x = 0
while x < 10:
    print(x)
    x += 1
```

#### For Loop with Range
```python
for i in range(10):      # 0 to 9
    print(i)

for i in range(5, 10):   # 5 to 9
    print(i)
```

### 6. Break & Continue
- `break` - exit the loop immediately
- `continue` - skip to next iteration

### 7. Functions
```python
def greet(name):
    print(f"Hello, {name}!")

def add(x, y):
    return x + y
```

- Functions can have multiple parameters
- Functions can return multiple values
- A function without `return` returns `None`

### 8. Local vs Global Variables
- Variables inside functions are **local**
- Use `global` keyword to modify global variables (use sparingly)

### 9. Random Module
```python
import random
x = random.randint(1, 10)  # random int from 1 to 10 (inclusive)
```

## Exercises
- **grades.py** - Grade calculator with if/elif/else
- **number_check.py** - Check if number is odd/even
- **random_guesser.py** - Number guessing game

