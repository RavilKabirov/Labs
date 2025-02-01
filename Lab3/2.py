class Shape:
    def __init__(self):
        self.length = 0 

    def area(self):
        print(0) 


class Square(Shape):  
    def __init__(self, length=0):
         
        self.length = length 

    def area(self):
        print(self.length * self.length) 



s1 = Shape()
s1.area() 


s2 = Square()
s2.area() 
