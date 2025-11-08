data = [((0, 0), 'red'),
        ((5, 5), 'blue'),
        ((10, 0), 'green')]

x = float(input("Enter x-val: "))
y = float(input("Enter y-val: "))

p = (x, y)

def distance(p1, p2):
    """
    Return the euclidean dist.
    between p1, p2
    """
    
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)

def classify(p):
    """
    If the point is already in data, return the color,
    if it is not, figure out its color, and add it to the
    data list, then return the color...
    
    For example, given p = (2, 2), we'd classify as 'red', and add
    ((2, 2), 'red') to data, then return 'red'
    """
    
    for point, color in data:
        if point == p:
            return color
        
    nearest_distance = float("inf") # some extremely large float value
    nearest_color = None
    
    for point, color in data:
        dist = distance(p, point)
        
        if dist < nearest_distance:
            nearest_distance = dist
            nearest_color = color
    
    data.append((p, nearest_color))
    
    return nearest_color
    
color = classify(p)
print(color)