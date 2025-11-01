import pandas as pd

# Series

scores = pd.Series([90, 85, 88], index=['Alice', 'Bob', 'Charlie'])

print(scores)
print(scores[0])
print(scores['Alice'])

# DataFrame

data = {'Name' : ['Alice', 'Bob', 'Charlie'],
        'Score': [90, 85, 88],
        'Age': [20, 21, 19]}

df = pd.DataFrame(data)

print()
print(df)
print(df.describe())

print()
print(scores.describe())

print(df[df['Score'] > 86]) # cuts rows such that Score <= 86