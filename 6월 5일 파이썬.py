#20191950 왕성민
import math

class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    def __neg__(self):
        return Vector2D(-self.x,-self.y) 
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y 
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    
v1 = Vector2D(1, 1)
v2 = Vector2D(1, 9)
v3 = v1 + v2
print(v1,'+',v2,'=', v3)

v3 = v1 - v2
print(v1,'-',v2,'=', v3)

v3 = v1 * v2
print(v1,'*',v2,'=', v3)

v3 = v1 / v2
print(v1,'/',v2,'=', v3)

v3 = -v1
print('-',v1,'=',v3)

v3 = v1 == v2

dist = v1.distance(v2)


print('Distance between', v1, 'and', v2, '=', dist)
print(v1,'==',v2,'=',v3)
print("20191950 왕성민")