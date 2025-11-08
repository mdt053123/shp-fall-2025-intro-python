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
    
    # first check if pt. exists
    for point, color in points:
        if point == p:
            return color
        
    # next, collect distances w/ index for tiebreaking + colors
    dists = []
    idx = 0
    for point, color in points:
        d = distance(point, p)
        dists.append((d, idx, color))
        idx += 1
        
    # sort distances
    dists_sorted = sorted(dists)
    
    # get k nearest neighbors
    k_neighbors = dists_sorted[:k]
    
    # find the number of appearances of each color
    counts = {}
    for _, _, color in k_neighbors:
        if color in counts:
            counts[color] += 1
        else:
            counts[color] = 1
    
    # find color with max count
    majority_color = None
    majority_count = -1
    for color, count in counts.items():
        if count > majority_count:
            majority_count = count
            majority_color = color
            
    # store + return
    points.append((p, majority_color))
    return majority_color