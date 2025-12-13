# Day 10: File I/O & Stock Market Analysis

## Topics Covered

### 1. File I/O

#### Writing to Files
```python
with open("output.txt", "w") as f:
    f.write("Hello, World\n")
    f.write("Line 2\n")
```

#### Reading Files
```python
with open("file.txt", "r") as f:
    content = f.read()      # entire file as string
    
with open("file.txt", "r") as f:
    for line in f:          # line by line
        print(line.strip())
```

#### Appending to Files
```python
with open("file.txt", "a") as f:
    f.write("New line\n")
```

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites) |
| `"a"` | Append |

### 2. Exception Handling
```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid integer!")
```

### 3. Enumerate Function
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### 4. Lambda Functions (Review)
```python
square = lambda x: x * x
greet = lambda name: f"Hello, {name}!"
```

### 5. Comprehensions

#### List Comprehension
```python
squares = [x*x for x in range(10)]
```

#### Dictionary Comprehension
```python
d = {x: x*x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Stock Market Analysis Project

### 1. Getting Stock Data
```python
import yfinance as yf

df = yf.download("AAPL", period="1y")
```

### 2. Stock Data Columns
- **Open** - price at market open
- **High** - highest price of the day
- **Low** - lowest price of the day
- **Close** - price at market close
- **Volume** - shares traded

### 3. Visualization
```python
import matplotlib.pyplot as plt

plt.plot(df['Close'])
plt.title("Stock Price")
plt.show()
```

### 4. Moving Averages
Smooth out price data to see trends.

```python
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
```

### 5. Prediction with Linear Regression
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Prepare data
df['Day'] = range(len(df))
df['Tomorrow'] = df['Close'].shift(-1)

X = df[['Day']]
y = df['Tomorrow']

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
```

### 6. Comparing Stocks (Normalization)
```python
normalized = (stock / stock.iloc[0]) * 100
```

## Key Takeaways
- `with` statement ensures files are properly closed
- Exception handling prevents crashes from bad input
- Stock prediction is difficult due to market complexity
- Simple models find trends but miss day-to-day movements

