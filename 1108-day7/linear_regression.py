x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

x_bar = sum(x) / len(x)
y_bar = sum(y) / len(y)

n = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
d = sum((xi - x_bar) ** 2 for xi in x)

m = n / d
b = y_bar - m * x_bar

print(f"y = {m}x + {b}")

y_pred = m*20 + b

print(f"For x = 20, we get y = {y_pred}...")