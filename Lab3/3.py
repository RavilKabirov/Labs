class Shape:
    def __init__(self):
        self.area = 0
    def Area(self):
        print(self.area)
       
class Rectangle(Shape):
    
    def __init__(self, width, length):
        
        self.area = length * width

s = Rectangle(2, 3)
s.Area()