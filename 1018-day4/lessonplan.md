# Day 4: Strings, Classes & Recursion

## Topics Covered

### 1. Types and Objects
- Everything in Python is an object
- Use `type()` to check the type of any value

### 2. Identity vs Equality
```python
x = [1, 2]
y = [1, 2]
z = x

x == y  # True (same values)
x is y  # False (different objects)
x is z  # True (same object)
```

### 3. String Slicing
Strings are sequences of characters.

```python
s = "Python"
s[0]      # 'P' (first character)
s[-1]     # 'n' (last character)
s[0:3]    # 'Pyt' (slice)
s[::-1]   # 'nohtyP' (reverse)
s[::2]    # 'Pto' (every 2nd character)
```

### 4. String Methods
| Method | Description |
|--------|-------------|
| `s.lower()` | Convert to lowercase |
| `s.upper()` | Convert to uppercase |
| `s.split(sep)` | Split into list |
| `sep.join(list)` | Join list into string |

### 5. Classes and Objects
Classes are blueprints for creating objects.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_info(self):
        return f"{self.name}: Grade {self.grade}"
```

#### Key Concepts
- `__init__` - constructor (called when creating object)
- `self` - reference to the current instance
- **Attributes** - data stored in the object
- **Methods** - functions that belong to the object

### 6. Dunder (Magic) Methods
| Method | Description |
|--------|-------------|
| `__init__` | Constructor |
| `__str__` | String representation |
| `__eq__` | Equality comparison (`==`) |
| `__getitem__` | Indexing (`obj[key]`) |

```python
def __eq__(self, other):
    return self.name == other.name
```

### 7. Recursion
A function that calls itself.

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
```

#### Key Components
- **Base case** - when to stop recursing
- **Recursive case** - calling the function with a smaller problem

## Exercises
- **student.py** - Complete Student class with methods
- **car.py** - Car class with equality comparison
- **exercises.py** - StringAnalyzer class (palindrome, vowels, contains)

