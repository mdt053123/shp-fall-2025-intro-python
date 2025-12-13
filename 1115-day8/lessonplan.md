# Day 8: Data Science in Practice

## Topics Covered

### 1. Python Data Structures Review
- Lists, sets, tuples, dictionaries

### 2. NumPy Deep Dive

#### Creating Arrays
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

zeros = np.zeros((3, 3), dtype=int)
ones = np.ones((7, 4), dtype=int)
rand = np.random.rand(3, 3)
arr = np.arange(10)  # [0, 1, 2, ..., 9]
```

#### Array Properties
| Property | Description |
|----------|-------------|
| `arr.shape` | Dimensions (rows, cols) |
| `arr.ndim` | Number of dimensions |

#### Slicing
```python
arr[2:4]  # elements 2 and 3
```

### 3. Dot Product & Matrix Multiplication
```python
u = np.array([1, 2, 3])
v = np.array([3, 0, 1])
u @ v  # dot product = 6

M1 @ M2  # matrix multiplication
```

### 4. Pandas DataFrames
```python
import pandas as pd

df = pd.DataFrame({
    "Name": ['Alice', 'Bob'],
    "Score": [88, 92]
})

df.head()       # first 5 rows
df.tail()       # last 5 rows
df.info()       # data types & non-null counts
df.describe()   # summary statistics
```

#### Filtering
```python
df[df["Age"] >= 21]           # rows where Age >= 21
df["Age"]                      # single column
df[["Name", "Score"]]          # multiple columns
```

### 5. Matplotlib Visualization
```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Title")
plt.show()

# Scatter plot
plt.scatter(x, y)

# Histogram
plt.hist(data, bins=30)
```

### 6. Machine Learning with Scikit-learn

#### Train/Test Split
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

#### KNN Classification
```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = knn.score(X_test, y_test)
```

### 7. Real Datasets
- **Breast Cancer Dataset** - binary classification
- **Iris Dataset** - multi-class classification

### 8. Hyperparameter Tuning
Experimenting with:
- **k value** - number of neighbors
- **test_size** - proportion of data for testing
- **random_state** - reproducibility seed

## Key Takeaways
- NumPy for numerical computation
- Pandas for data manipulation
- Matplotlib for visualization
- Scikit-learn for machine learning

