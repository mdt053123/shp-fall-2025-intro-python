data = [((0, 0), 'red'),
        ((5, 5), 'blue'),
        ((10, 0), 'green'),
        ((10, 1), 'green')]

x = float(input("Enter x-val: "))
y = float(input("Enter y-val: "))

p = (x, y)

def distance(p1, p2):
    """
    Return the euclidean dist.
    between p1, p2
    """
    
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)

def classify(p, k):
    """
    Can assume: k % 2 == 1 (odd), k <= len(data)
    """