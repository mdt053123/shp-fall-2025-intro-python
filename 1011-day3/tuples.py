t1 = (3, 4, 5)
t2 = (5, 4, 3)

#print(t1)
#print(t2)

p1 = (2, 1)
p2 = (3, 4)

def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)

print(p1, p2)
print(dist(p1, p2))

t = (3,) # need comma for one-element tuple
print(type(t))