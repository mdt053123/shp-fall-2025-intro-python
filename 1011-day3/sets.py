my_set = {3, 4, 5, 5, 6}

print(my_set)
print(type(my_set))

my_set.add(7)
print(my_set)

s1 = {3, 4, 5}
s2 = {3, 4}

print()
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s2.issubset(s1))
print(s1.issubset(s1))