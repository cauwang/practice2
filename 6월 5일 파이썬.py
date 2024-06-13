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
    
class Line2D:
    def __init__(self, vector1, voctor2):
        self.__vector1 = vector1
        self.__voctor2 = voctor2

    def __len__(self):
        return int(self.__vector1.distance(self.__voctor2))

    def __eq__(self, other):
        if isinstance(other, Line2D):
            return self.__vector1 == other.__vector1 and self.__voctor2 == other.__voctor2
        return False

    def __lt__(self, other):
        return self.__vector1.distance(self.__voctor2) < other.__vector1.distance(other.__voctor2)

    def __le__(self, other):
        return self.__vector1.distance(self.__voctor2) <= other.__vector1.distance(other.__voctor2)

    def __gt__(self, other):
        return self.__vector1.distance(self.__voctor2) > other.__vector1.distance(other.__voctor2)

    def __ge__(self, other):
        return self.__vector1.distance(self.__voctor2) >= other.__vector1.distance(other.__voctor2)

    def __str__(self):
        return "{} - {}".format(self.__vector1, self.__voctor2)

    def length(self):
        return self.__vector1.distance(self.__voctor2)    
    

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


v5 = Vector2D(0, 0)
v6 = Vector2D(1, 1)
line1 = Line2D(v5, v6)

v7 = Vector2D(1, 1)
v8 = Vector2D(4, 5)
line2 = Line2D(v7, v8)

print("Line1 length using len():", len(line1))
print("Line1 length using length method:", line1.length())

print("Line1 == Line2:", line1 == line2)
print("Line1 < Line2:", line1 < line2)
print("Line1 <= Line2:", line1 <= line2)
print("Line1 > Line2:", line1 > line2)
print("Line1 >= Line2:", line1 >= line2)

print("Line1:", line1)
print("Line2:", line2)

print("20191950 왕성민")