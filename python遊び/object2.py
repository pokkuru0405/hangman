##class Shape:
##    def __init__(self,w,h):
##        self.width = w
##        self.high = h
##
##    def what_am_i(self):
##        print("I am shape")
##
##class Rectangle(Shape):
##    def __init__(self,w,h):
##        self.width = w
##        self.high = h
##    def calculate_perimeter(self):
##        return self.width * 2 + self.high * 2
##
##class Square(Shape):
##    def __init__(self,l):
##        self.long = l
##
##    def calculate_perimeter(self):
##        return self.long * 4
##
##    def change_size(self,k):
##        self.long = self.long + k
##        
##
##rectangle = Rectangle(2,4)
##print(rectangle.calculate_perimeter())
##square = Square(4)
##square.change_size(-3)
##print(square.calculate_perimeter())
##
##rectangle.what_am_i()
##square.what_am_i()
##
##
##class Hope:
##    def __init__(self,owner):
##        self.owner = owner
##
##class Rider:
##    def __init__(self,name):
##        self.name = name
##
##mick = Rider("micky")
##hope = Hope(mick)
##print(hope.owner.name)
##
##
##
##

class Square:
    rec = []

    def __init__(self,l):
        self.long = l
        self.rec.append(self.long)

    def calculate_perimeter(self):
        return self.long * 4

    def change_size(self,k):
        self.long = self.long + k

    def print_size(self):
        print("{}by{}by{}by{}".format(self.long,self.long,self.long,self.long))

s1 = Square(2)
s2 = Square(4)
print(Square.rec)
s1.print_size()

def zengo(x,y):
    print(x is y)
    
a = input("ひとつめ")
b = input("ふたつめ")
zengo(a,b)
