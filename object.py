class Apple:
    def __init__(self,w,c,a,d):
        self.weight = w
        self.color = c
        self.amasa = a
        self.days = d
        print("できたよ")

apple = Apple(200,"真っ赤",45,3)
print(apple.color)

class Circle:    
    def __init__(self,h):
        self.hankei = h

    def area(self):
        return self.hankei ** 2 * math.pi
import math
circle = Circle(3)
print(circle.area())

    
class Triangle:
    def __init__(self,t,h):
        self.teihen = t
        self.high =  h

    def area(self):
        return self.teihen * self.high / 2
triangle = Triangle(2,3)
print(triangle.area())


class Hexagon:
    def __init__(self,l):
        self.long = l

    def calculate_perimeter(self):
        return self.long * 6
hexagon = Hexagon(6)
print(hexagon.calculate_perimeter())
