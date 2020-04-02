import math
 
def line_intersect(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return -100000, -100000

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


class Field():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.foods = None
    
    def draw(self):
        rectMode(CORNERS)
        fill(240)
        rect(self.x1, self.y1, self.x2, self.y2)
    
    def place_food(self, foods):
        self.foods = foods
    
    def nearest_food(self, x, y):
        
        #index_min = min(range(len(self.food)), key=values.__getitem__)
        _, food = min(enumerate(self.foods), key=lambda f: math.sqrt((f[1].x - x)**2 +(f[1].y - y)**2))

        return food, math.sqrt((food.x - x)**2 +(food.y - y)**2)

        
        
    def check_border(self, xprev, yprev, vx, vy):
        # top border
        xi, yi = line_intersect([[xprev, yprev], [xprev + vx, yprev + vy]],
                                [[self.x1, self.y1], [self.x2, self.y1]])
        if xi > self.x1 and xi < self.x2 and yprev + vy < self.y1:
            return vx, vy + (self.y2 - self.y1)
        # bottom border
        xi, yi = line_intersect([[xprev, yprev], [xprev + vx, yprev + vy]],
                                [[self.x1, self.y2], [self.x2, self.y2]])
        if xi > self.x1 and xi < self.x2 and yprev + vy > self.y2:
            return vx, vy - (self.y2 - self.y1)
        # left border
        xi, yi = line_intersect([[xprev, yprev], [xprev + vx, yprev + vy]],
                                [[self.x1, self.y1], [self.x1, self.y2]])
        if yi > self.y1 and yi < self.y2 and xprev + vx < self.x1:
            return vx + (self.x2 - self.x1), vy
        # right border
        xi, yi = line_intersect([[xprev, yprev], [xprev + vx, yprev + vy]],
                                [[self.x2, self.y1], [self.x2, self.y2]])
        if yi > self.y1 and yi < self.y2 and xprev + vx > self.x2:
            return vx - (self.x2 - self.x1), vy
        return vx, vy
