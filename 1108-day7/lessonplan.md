# Day 7: Machine Learning Fundamentals

## Topics Covered

### 1. Euclidean Distance
Distance between two points in space.

```python
def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)
```

### 2. Nearest Neighbor Classification
Classify a point based on the label of its closest neighbor.

```python
def classify(p):
    nearest_distance = float("inf")
    nearest_color = None
    
    for point, color in data:
        dist = distance(p, point)
        if dist < nearest_distance:
            nearest_distance = dist
            nearest_color = color
    
    return nearest_color
```

### 3. K-Nearest Neighbors (KNN)
Instead of just the closest neighbor, use **k** neighbors and take a majority vote.

**Steps:**
1. Calculate distance to all points
2. Sort by distance
3. Take the k nearest neighbors
4. Return the most common label

### 4. Linear Regression (From Scratch)
Find the best-fit line: **y = mx + b**

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

x_bar = sum(x) / len(x)
y_bar = sum(y) / len(y)

n = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
d = sum((xi - x_bar) ** 2 for xi in x)

m = n / d                   # slope
b = y_bar - m * x_bar       # intercept
```

### 5. Scikit-learn
Python's machine learning library.

#### KNN with sklearn
```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data[['x', 'y']], data['color'])
knn.predict([[3, 2]])
```

#### Linear Regression with sklearn
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
print(f"m = {model.coef_}, b = {model.intercept_}")
```

## Key Concepts
- **Classification** - predicting a category/label
- **Regression** - predicting a continuous value
- **Training data** - data used to build the model
- **Features (X)** - input variables
- **Target (y)** - what we're predicting

